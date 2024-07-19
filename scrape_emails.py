import re

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def scrape_emails(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", soup.text))

        with open('emails.txt', 'a') as file:  # Ensure 'a' mode is used to append
            for email in emails:
                file.write(email + '\n')

        print(f"Found and saved {len(emails)} email(s) to emails.txt")
    except requests.RequestException as e:
        print(f"Failed to retrieve the web page. Error: {e}")

@app.route('/save_emails', methods=['POST'])
def handle_save_emails():
    data = request.get_json()
    url = data.get('url')
    if url:
        scrape_emails(url)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error", "message": "No URL provided"}), 400

if __name__ == '__main__':
    app.run(port=5000)
