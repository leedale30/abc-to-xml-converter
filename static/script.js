document.addEventListener('DOMContentLoaded', () => {
    const convertBtn = document.getElementById('convert-btn');
    const downloadBtn = document.getElementById('download-btn');
    const copyBtn = document.getElementById('copy-btn');
    const inputArea = document.getElementById('abc-input');
    const outputArea = document.getElementById('output-xml');
    const statusText = document.getElementById('status-text');
    const statusDot = document.getElementById('status-dot');

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
                document.getElementById('output-logs').value = data.logs || 'No warnings found.';
                updateStatus('Conversion Successful', 'success');
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
