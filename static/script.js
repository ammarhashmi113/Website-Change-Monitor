function checkStatus() {
    fetch('/check')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const statusElement = document.getElementById('status');
                if (data.is_open) {
                    statusElement.textContent = 'Change In Webpage Detected';
                } else {
                    statusElement.textContent = 'No Change Detected';
                }
            } else {
                console.error('Error:', data.message);
            }
        })
        .catch(error => console.error('Error:', error));
}

setInterval(checkStatus, 5000);
checkStatus();
