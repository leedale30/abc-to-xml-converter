document.addEventListener('DOMContentLoaded', () => {
    const convertBtn = document.getElementById('convert-btn');
    const downloadBtn = document.getElementById('download-btn');
    const copyBtn = document.getElementById('copy-btn');
    const inputArea = document.getElementById('abc-input');
    const outputArea = document.getElementById('output-xml');
    const statusText = document.getElementById('status-text');
    const statusDot = document.getElementById('status-dot');

    // OSMD Elements
    const viewCodeBtn = document.getElementById('view-code-btn');
    const viewSheetBtn = document.getElementById('view-sheet-btn');
    const sheetContainer = document.getElementById('osmd-container');
    const playbackControls = document.getElementById('playback-controls');
    const playBtn = document.getElementById('play-btn');
    const stopBtn = document.getElementById('stop-btn');
    const bpmInput = document.getElementById('bpm-input');

    let osmd = null;
    let isPreviewMode = false;
    let playbackTimeout = null;
    let isPlaying = false;
    let currentXml = ""; // Store current XML for rendering logic

    const updateStatus = (text, type) => {
        statusText.textContent = text;
        statusDot.className = `status-dot ${type}`;
    };

    convertBtn.addEventListener('click', async () => {
        const abcContent = inputArea.value;

        if (!abcContent.trim()) {
            updateStatus('Please enter ABC notation', 'error');
            return;
        }

        updateStatus('Converting...', 'processing');
        outputArea.value = ''; // Clear previous output

        try {
            const response = await fetch('/convert', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ abc_content: abcContent }),
            });

            const data = await response.json();

            if (response.ok) {
                outputArea.value = data.xml_content;
                currentXml = data.xml_content; // Update current XML
                document.getElementById('output-logs').value = data.logs || 'No warnings found.';
                updateStatus('Conversion Successful', 'success');

                // If in preview mode, render immediately
                if (isPreviewMode) {
                    renderSheet();
                }

            } else {
                updateStatus('Conversion Failed', 'error');
                outputArea.value = 'Error:\n' + (data.error || 'Unknown error');
                document.getElementById('output-logs').value = data.error || '';
            }
        } catch (error) {
            updateStatus('Network Error', 'error');
            outputArea.value = 'Error: ' + error.message;
        }
    });

    // --- OSMD & Playback Logic ---

    // Initialize OSMD on first need
    const initOSMD = () => {
        if (!osmd) {
            osmd = new opensheetmusicdisplay.OpenSheetMusicDisplay("osmd-container", {
                autoResize: true,
                backend: "svg",
                drawingParameters: "compacttight", // Try to fit more
                drawTitle: true,
                followCursor: true, // Auto-scroll
            });
        }
    };

    const renderSheet = async () => {
        if (!currentXml) return;

        try {
            initOSMD();

            // Show loading state if complex? 
            // osmd.load() can be async
            await osmd.load(currentXml);
            osmd.render();

            // Reset cursor
            osmd.cursor.reset();
            osmd.cursor.show();

        } catch (e) {
            console.error("OSMD Render Error:", e);
            updateStatus("Error Rendering Sheet Music", "error");
        }
    };

    // View Toggle
    const setViewMode = (mode) => {
        if (mode === 'code') {
            isPreviewMode = false;
            viewCodeBtn.classList.add('active');
            viewSheetBtn.classList.remove('active');
            outputArea.classList.remove('hidden');
            sheetContainer.classList.add('hidden');
            playbackControls.classList.add('hidden');
            stopPlayback();
        } else { // sheet
            isPreviewMode = true;
            viewCodeBtn.classList.remove('active');
            viewSheetBtn.classList.add('active');
            outputArea.classList.add('hidden');
            sheetContainer.classList.remove('hidden');
            playbackControls.classList.remove('hidden'); // Show controls

            // If we have content but haven't rendered or it's new
            // For simplicity, just try rendering if we have XML
            // We use outputArea value as source of truth if manual edits happened
            if (outputArea.value && outputArea.value !== currentXml) {
                currentXml = outputArea.value;
            }

            if (currentXml) {
                renderSheet();
            }
        }
    };

    viewCodeBtn.addEventListener('click', () => setViewMode('code'));
    viewSheetBtn.addEventListener('click', () => setViewMode('sheet'));

    // --- Audio Playback Logic using ABCJS ---

    let synth = null;
    let audioContext = null;
    let playbackInterval = null;

    const logToUI = (msg) => {
        const logsArea = document.getElementById('output-logs');
        logsArea.value += `[Audio] ${msg}\n`;
        logsArea.scrollTop = logsArea.scrollHeight;
        console.log(`[Audio] ${msg}`);
    };

    const startPlayback = async () => {
        if (!window.ABCJS) {
            updateStatus('ABCJS Audio Library not loaded', 'error');
            logToUI('ABCJS not found in window object.');
            return;
        }

        if (isPlaying) {
            logToUI('Already playing, ignoring start request.');
            return;
        }

        // 1. Initialize Audio Context if needed
        if (!audioContext) {
            try {
                audioContext = new (window.AudioContext || window.webkitAudioContext)();
                logToUI(`AudioContext created. State: ${audioContext.state}`);
            } catch (e) {
                logToUI(`Failed to create AudioContext: ${e.message}`);
                updateStatus('Audio Support Failed', 'error');
                return;
            }
        }
        if (audioContext.state === 'suspended') {
            try {
                await audioContext.resume();
                logToUI('AudioContext resumed.');
            } catch (e) {
                logToUI(`Failed to resume AudioContext: ${e.message}`);
            }
        }

        // 2. Prepare Synth
        if (!synth) {
            synth = new ABCJS.synth.CreateSynth();
            logToUI('Synth instance created.');
        }

        const abcContent = inputArea.value;
        if (!abcContent.trim()) {
            updateStatus('No ABC content to play', 'error');
            return;
        }

        updateStatus('Preparing Audio...', 'processing');
        playBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
        logToUI('Starting playback sequence...');

        try {
            // We need a visual Obj for the synth to work, but we don't need to display it.
            // Render to a virtual element or just get the object
            const visualObjArr = ABCJS.renderAbc("*", abcContent, {
                add_classes: true,
                responsive: "resize"
            });

            if (!visualObjArr || visualObjArr.length === 0) {
                logToUI('ABCJS renderAbc returned no visual objects.');
                throw new Error("Could not parse ABC for audio.");
            }

            const visualObj = visualObjArr[0];

            let durationSec = 10; // Default fallback
            if (visualObj && typeof visualObj.getTotalTime === 'function') {
                const totalTime = visualObj.getTotalTime();
                if (typeof totalTime === 'number' && !isNaN(totalTime)) {
                    durationSec = totalTime;
                }
            }
            logToUI(`Visual Object created. Total Duration: ${durationSec}s (original: ${visualObj ? visualObj.getTotalTime() : 'N/A'})`);

            if (durationSec === 0) {
                logToUI('Duration is 0. Attempting to play anyway.');
                durationSec = 10;
            }

            logToUI('Initializing Synth...');
            await synth.init({
                audioContext: audioContext,
                visualObj: visualObj,
            });

            logToUI('Priming Synth (loading buffers)...');
            await synth.prime();

            isPlaying = true;
            synth.start();
            logToUI('Synth started.');

            updateStatus('Playing...', 'processing');
            playBtn.innerHTML = '<i class="fa-solid fa-stop"></i>';

            // Approximate Cursor Movement (Visual Sync is hard between libraries)
            if (osmd) {
                osmd.cursor.show();
                if (osmd.cursor.Iterator.EndReached) osmd.cursor.reset();

                // Simple Interval based on BPM input just for visuals
                const bpm = parseInt(bpmInput.value, 10) || 100;
                const msPerBeat = 60000 / bpm;

                if (playbackInterval) clearInterval(playbackInterval);
                playbackInterval = setInterval(() => {
                    if (osmd && isPlaying) {
                        try {
                            osmd.cursor.next();
                            if (osmd.cursor.Iterator.EndReached) {
                                // Don't auto stop synth, let synth finish
                            }
                        } catch (e) { }
                    }
                }, msPerBeat);
            }

            // Detect end
            const durationMs = durationSec * 1000;
            logToUI(`Scheduled stop in ${durationMs + 1000}ms`);
            setTimeout(() => {
                if (isPlaying) {
                    logToUI('Track finished (timeout).');
                    stopPlayback();
                }
            }, durationMs + 1000);

        } catch (error) {
            console.error("Audio Error:", error);
            logToUI(`EXCEPTION: ${error.message}`);
            updateStatus('Audio Error: ' + error.message, 'error');
            stopPlayback();
        }
    };

    const stopPlayback = () => {
        isPlaying = false;
        if (synth) {
            synth.stop();
        }
        if (playbackInterval) {
            clearInterval(playbackInterval);
            playbackInterval = null;
        }
        if (osmd) {
            osmd.cursor.reset();
            osmd.cursor.show(); // keep cursor visible at start
        }
        updateStatus('Ready', 'success');
        playBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
    };

    // Toggle Play/Pause
    playBtn.addEventListener('click', () => {
        if (isPlaying) {
            stopPlayback();
        } else {
            startPlayback();
        }
    });

    stopBtn.addEventListener('click', stopPlayback);

    copyBtn.addEventListener('click', () => {
        if (!outputArea.value) return;
        navigator.clipboard.writeText(outputArea.value).then(() => {
            const originalText = statusText.textContent;
            updateStatus('Copied to clipboard!', 'success');
            setTimeout(() => {
                updateStatus(originalText, originalText.includes('Success') ? 'success' : 'processing');
            }, 2000);
        });
    });

    const saveSessionBtn = document.getElementById('save-session-btn');
    if (saveSessionBtn) {
        saveSessionBtn.addEventListener('click', async () => {
            if (!outputArea.value) {
                updateStatus('Nothing to save', 'error');
                return;
            }

            updateStatus('Saving session...', 'processing');
            const logsValue = document.getElementById('output-logs').value;

            try {
                const response = await fetch('/save', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        abc_content: inputArea.value,
                        xml_content: outputArea.value,
                        logs: logsValue
                    })
                });

                const data = await response.json();
                if (response.ok) {
                    updateStatus('Saved to ' + data.path, 'success');
                    // Reset status text after 5 seconds because path is long
                    setTimeout(() => updateStatus('Ready', 'processing'), 5000);
                } else {
                    updateStatus('Save Failed: ' + data.error, 'error');
                }
            } catch (error) {
                updateStatus('Network Error during save', 'error');
            }
        });
    }

    const copyLogsBtn = document.getElementById('copy-logs-btn');
    if (copyLogsBtn) {
        copyLogsBtn.addEventListener('click', () => {
            const logsArea = document.getElementById('output-logs');
            if (!logsArea.value) return;
            navigator.clipboard.writeText(logsArea.value).then(() => {
                updateStatus('Logs copied!', 'success');
                setTimeout(() => {
                    updateStatus('Ready', 'processing');
                }, 2000);
            });
        });
    }

    downloadBtn.addEventListener('click', () => {
        if (!outputArea.value) return;
        const blob = new Blob([outputArea.value], { type: 'application/octet-stream' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'output.musicxml';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    });

    // Download Debug Report (combined MD file)
    const downloadDebugBtn = document.getElementById('download-debug-btn');
    if (downloadDebugBtn) {
        downloadDebugBtn.addEventListener('click', () => {
            const abcContent = inputArea.value || '(empty)';
            const xmlContent = outputArea.value || '(empty)';
            const logsContent = document.getElementById('output-logs').value || 'No logs';

            // Extract title from ABC content if available
            const titleMatch = abcContent.match(/^T:\s*(.*)$/m);
            const title = titleMatch ? titleMatch[1].trim() : 'Untitled';
            const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);

            const mdContent = `# ABC+ Converter Debug Report

**Title:** ${title}  
**Date:** ${new Date().toLocaleString()}

---

## ABC+ Input

\`\`\`abc
${abcContent}
\`\`\`

---

## MusicXML Output

\`\`\`xml
${xmlContent}
\`\`\`

---

## Validation Log

\`\`\`
${logsContent}
\`\`\`
`;

            const blob = new Blob([mdContent], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `debug_${timestamp}_${title.replace(/[^a-zA-Z0-9]/g, '_')}.md`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            updateStatus('Debug report downloaded', 'success');
            setTimeout(() => updateStatus('Ready', ''), 2000);
        });
    }

    // Auto-focus input
    inputArea.focus();

    // Check for updates on startup
    async function checkForUpdates() {
        try {
            const response = await fetch('/check-update');
            const data = await response.json();

            if (data.update_available) {
                const banner = document.getElementById('update-banner');
                const versionSpan = document.getElementById('latest-version');
                const downloadLink = document.getElementById('update-link');

                versionSpan.textContent = `v${data.latest_version}`;
                downloadLink.href = data.download_url;
                banner.classList.remove('hidden');
            }
        } catch (error) {
            // Silently fail - update check is not critical
            console.log('Update check failed:', error);
        }
    }

    // Dismiss update banner
    const dismissBtn = document.getElementById('dismiss-update');
    if (dismissBtn) {
        dismissBtn.addEventListener('click', () => {
            document.getElementById('update-banner').classList.add('hidden');
        });
    }

    // Run update check
    checkForUpdates();
});
