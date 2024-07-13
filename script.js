// const fs = require('fs')

document.addEventListener('DOMContentLoaded', function() {
    const inputElement = document.querySelector('.Input_s');
    const submitButton = document.querySelector('.Button_s');
    const responseElement = document.querySelector('.Response_s');

    submitButton.addEventListener('click', function() {
        const inputValue = inputElement.value;
        // fetch('http://127.0.0.1:5000/convert', {
        fetch('http://78.60.133.53:5001/convert', { // Use the IP address of the server (e.g. ')
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ link: inputValue }),
        })
        // .then(response => response.json()) 
        .then(response => {
            // Extract filename from Content-Disposition header
            const contentDisposition = response.headers.get('Content-Disposition');
            let filename = "Download.mp3"; // A default filename if none is found
            if (contentDisposition){ //&& contentDisposition.indexOf('attachment') !== -1) {
                const filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                const matches = filenameRegex.exec(contentDisposition);
                if (matches != null && matches[1]) { 
                    filename = matches[1].replace(/['"]/g, '');
                }
            } 
            return response.blob().then(blob => ({blob, filename}));
        })
        .then(({blob, filename}) => {
            const mp3Blob = new Blob([blob], { type: 'audio/mpeg' });
            const url = window.URL.createObjectURL(mp3Blob);
            // Create an <a> element for the download
            const a = document.createElement('a');
            a.href = url;
            a.download = filename; // Use the extracted filename for the download
            document.body.appendChild(a); // Append the <a> element to the document
            a.click(); // Programmatically
            window.URL.revokeObjectURL(url); // Revoke the Blob URL
            a.remove(); // Clean up the <a> element
            })
        .catch((error) => {
            console.error('Error:', error);
            // responseElement.textContent = 'Error: Could not get a response from the server.';
            responseElement.textContent = error;
        });
    });
});