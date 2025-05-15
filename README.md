# Pastebin Keyword Crawler

## Overview

**Pastebin Keyword Crawler** is a Python script that scrapes Pastebin's public archive for pastes containing crypto-related keywords or Telegram links. It extracts relevant information and saves it in a structured JSON Lines format. The application is built using Streamlit, allowing a user-friendly interface for initiating and viewing the crawling process.

## Features

- Scrapes the latest 30 pastes from Pastebin's archive.
- Searches for keywords related to cryptocurrencies and Telegram links.
- Outputs results in a JSON Lines file (`keyword_matches.jsonl`).
- Implements rate-limiting to avoid being blocked.
- Uses logging to record activities and keyword findings.
- Supports multi-threading for faster processing.

## Requirements

- Python 3.7 or higher
- `requests` library
- `beautifulsoup4` library
- `streamlit` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/BTANISHA11/pastebin-keyword-crawler.git
    cd pastebin-keyword-crawler
    ```

2. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

   Ensure your `requirements.txt` includes the following:
## Usage

1. **Run the application**:
Use the Streamlit command to start the application.

 ```bash
 streamlit run app.py
 ```

2. **Access the interface**:
- Open a web browser and navigate to `http://localhost:8501`.
- Click "Start Crawling" to begin fetching and analyzing pastes from Pastebin.

3. **View results**:
- Results will be displayed within the Streamlit app and saved to `keyword_matches.jsonl`.

## Configuration

- **Rate Limiting**: Adjust the sleep interval between requests in the script for different rate-limiting needs.
- **Proxies**: If you have access to a pool of proxies, you can configure them within the script to enhance anonymity and circumvent rate limits.

## Logging

Log files will record each paste accessed and any keywords found during the crawling process. This can help with debugging and tracking script activity.

## Contribution

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
