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
                updateStatus('Conversion Successful', 'success');
            } else {
                updateStatus('Conversion Failed', 'error');
                outputArea.value = 'Error:\n' + (data.error || 'Unknown error');
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

    downloadBtn.addEventListener('click', () => {
        if (!outputArea.value) return;
        const blob = new Blob([outputArea.value], { type: 'text/xml' });
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
