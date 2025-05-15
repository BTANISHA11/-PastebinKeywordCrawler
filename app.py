import streamlit as st
import requests
from bs4 import BeautifulSoup
import json
import time
import logging
import threading
from datetime import datetime

# Define keywords to search for
keywords = ["crypto", "bitcoin", "ethereum", "blockchain", "t.me"]

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to obtain the latest 30 paste IDs from Pastebin's archive
def get_paste_ids():
    archive_url = "https://pastebin.com/archive"
    response = requests.get(archive_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paste_ids = [link['href'].split('/')[-1] for link in soup.find_all('a', href=True) if link['href'].startswith('/')]
        return paste_ids[:30]
    else:
        st.error("Failed to retrieve Pastebin archive")
        return []

# Function to fetch and analyze paste content
def fetch_and_analyze_paste(paste_id, results):
    try:
        raw_url = f"https://pastebin.com/raw/{paste_id}"
        
        # Insert delay to avoid rate limiting
        time.sleep(1)

        # Optionally, request through a proxy: 
        proxies = {
            # 'http': 'http://your_proxy:port',
            # 'https': 'https://your_proxy:port',
        }
        response = requests.get(raw_url, proxies=proxies)
        
        if response.status_code == 200:
            content = response.text
            found_keywords = [keyword for keyword in keywords if keyword in content.lower()]
            if found_keywords:
                result = {
                    "source": "pastebin",
                    "context": f"Found crypto-related content in Pastebin paste ID {paste_id}",
                    "paste_id": paste_id,
                    "url": raw_url,
                    "discovered_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "keywords_found": found_keywords,
                    "status": "pending"
                }
                results.append(result)
                logging.info(f"Keywords found in paste ID {paste_id}: {found_keywords}")
        else:
            logging.warning(f"Failed to retrieve content for paste ID {paste_id}")
            
    except Exception as e:
        logging.error(f"Error processing paste ID {paste_id}: {e}")

# Multi-threading function
def crawl_pastes(paste_ids):
    results = []
    threads = []
    
    for paste_id in paste_ids:
        thread = threading.Thread(target=fetch_and_analyze_paste, args=(paste_id, results))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    # Write each JSON object to a new line in the output file
    with open('keyword_matches.jsonl', 'w') as file:
        for item in results:
            file.write(json.dumps(item) + '\n')
    
    return results

# Streamlit app function
def main():
    st.title("Pastebin Keyword Crawler")
    st.write("Scrape Pastebin for crypto and Telegram-related keywords with enhanced features.")

    if st.button("Start Crawling"):
        paste_ids = get_paste_ids()
        
        with st.spinner("Fetching and analyzing pastes..."):
            results = crawl_pastes(paste_ids)
        
        st.success("Crawling completed!")
        st.json(results)

        st.info("Results have been saved to keyword_matches.jsonl")

if __name__ == "__main__":
    main()