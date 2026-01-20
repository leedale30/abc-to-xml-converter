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

    // --- Ulthrathink Playback Logic ---

    const getBPM = () => {
        const bpm = parseInt(bpmInput.value, 10);
        return (bpm && bpm > 0) ? bpm : 100;
    };

    const playNextNote = () => {
        if (!osmd || !isPlaying) return;

        // Advance cursor
        const nextNoteExists = osmd.cursor.next();

        if (!nextNoteExists) {
            // End of score
            stopPlayback();
            return;
        }

        // Calculate duration for the *current* cursor position (after next() call)
        // Actually, cursor.next() places us visually on the note.
        // We should wait *before* moving to the next.
        // Wait... standard player logic:
        // 1. Show cursor at start.
        // 2. Wait for duration of note at start.
        // 3. Move to next.

        // But logic above calls next() first.
        // Let's adjust:
        // 1. We are at a position.
        // 2. Get duration of current notes under cursor.
        // 3. Wait that duration.
        // 4. Move next. If no next, stop.

        // Get current iterator notes
        const iterator = osmd.cursor.Iterator;
        // osmd.cursor.next() moved us to this new position.
        // We want to verify we are valid.

        if (iterator.EndReached) {
            stopPlayback();
            return;
        }

        // Calculate duration
        // CurrentVoiceEntries gives notes at this timestamp.
        // We take the max duration of notes here to determine step?
        // Actually we should use the iterator's timestamp diff?
        // OSMD Iterator is complex. 
        // Simplest Robust Logic: Notes[0].Length.RealValue (e.g., 0.25)

        let durationValue = 0.25; // Default quarter note fallback

        const voices = iterator.CurrentVoiceEntries;
        if (voices && voices.length > 0) {
            const voice = voices[0];
            if (voice.Notes && voice.Notes.length > 0) {
                // Use the first note's length. 
                // RealValue is fraction of whole note (0.25 = quarter)
                durationValue = voice.Notes[0].Length.RealValue;
            }
        }

        // Calculate milliseconds
        // BPM = Quarter notes per minute
        // 1 Quarter note (0.25) = 60000 / BPM ms
        // Duration (1.0) = 4 * (60000/BPM)
        // Duration (RealValue) = RealValue * 4 * (60000/BPM)

        const bpm = getBPM();
        const msPerQuarter = 60000 / bpm;
        const delay = durationValue * 4 * msPerQuarter;

        // Schedule next move
        playbackTimeout = setTimeout(playNextNote, delay);
    };

    const startPlayback = () => {
        if (!osmd) return;

        if (isPlaying) {
            // Already playing, ignore or pause?
            return;
        }

        isPlaying = true;
        osmd.cursor.show();

        // If cursor is at end, reset
        if (osmd.cursor.Iterator.EndReached) {
            osmd.cursor.reset();
        }

        // Start the loop
        // If we are at the very beginning (or reset), we should wait for the first note's duration
        // BEFORE moving. But playNextNote moves *first*.
        // So we need to handle the "current" note first.

        // Setup for first note:
        // 1. Display cursor (done)
        // 2. Get duration of *current* note (at start)
        // 3. Wait, then playNextNote (which moves)

        // Check current duration at start
        let durationValue = 0.25;
        try {
            const voices = osmd.cursor.Iterator.CurrentVoiceEntries;
            if (voices && voices.length > 0 && voices[0].Notes.length > 0) {
                durationValue = voices[0].Notes[0].Length.RealValue;
            }
        } catch (e) { console.log(e); }

        const bpm = getBPM();
        const msPerQuarter = 60000 / bpm;
        const delay = durationValue * 4 * msPerQuarter;

        updateStatus(`Playing (${bpm} BPM)...`, 'processing');
        playBtn.innerHTML = '<i class="fa-solid fa-pause"></i>'; // Change to pause icon logic?
        // Actually let's just keep Play/Stop for simplicity or toggle

        playbackTimeout = setTimeout(playNextNote, delay);
    };

    const stopPlayback = () => {
        isPlaying = false;
        if (playbackTimeout) {
            clearTimeout(playbackTimeout);
            playbackTimeout = null;
        }
        if (osmd) {
            osmd.cursor.reset();
            osmd.cursor.show();
        }
        updateStatus('Ready', 'success');
        playBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
    };

    // Toggle Play/Pause on play btn
    playBtn.addEventListener('click', () => {
        if (isPlaying) {
            // Pause logic (just clear timeout but don't reset)
            isPlaying = false;
            if (playbackTimeout) clearTimeout(playbackTimeout);
            updateStatus('Paused', 'processing');
            playBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
        } else {
            // Resume
            // If just paused, we should ideally wait remaining time, but
            // for visual cursor, immediate resume is fine.
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
