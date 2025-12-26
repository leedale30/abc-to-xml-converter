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

    // Auto-focus input
    inputArea.focus();
});
