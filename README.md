# Email Scraper Application

This project is an email scraper that captures email addresses from websites you visit in your browser and saves them to a text file (`emails.txt`). It consists of a Flask server (`scrape_emails.py`) and a browser extension that interacts with the server.

## Table of Contents

1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Flask Server](#flask-server)
4. [Browser Extension](#browser-extension)
5. [How to Use](#how-to-use)
6. [Troubleshooting](#troubleshooting)

## Overview

The application consists of two main components:
1. **Flask Server**: Handles incoming requests and processes URLs to extract email addresses.
2. **Browser Extension**: Monitors your browsing activity and sends URLs of visited websites to the Flask server for email extraction.

### Files
- `scrape_emails.py`: The Flask server script that scrapes emails from given URLs.
- `emails.txt`: The file where extracted email addresses are saved.
- `manifest.json`: The manifest file for the browser extension.
- `content.js`: The content script for the browser extension.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- Requests
- BeautifulSoup4
- Flask-CORS (to handle Cross-Origin Resource Sharing issues)
- A Chromium-based browser (Chrome, Brave, etc.)

### Step 1: Install Dependencies

Install the necessary Python libraries using pip:

```sh
pip install flask requests beautifulsoup4 flask-cors
