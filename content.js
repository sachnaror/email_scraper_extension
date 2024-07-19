function extractEmails(text) {
    return text.match(/[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g);
}

const emails = extractEmails(document.body.innerText);
if (emails && emails.length > 0) {
    console.log(`Extracted emails: ${emails}`);
    fetch('http://localhost:5000/save_emails', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: document.URL })
    })
        .then(response => response.json())
        .then(data => console.log('Response:', data))
        .catch(error => console.error('Error:', error));
}
