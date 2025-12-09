import requests
import sys
from datetime import datetime
from urllib.parse import quote

def fetch_summary(keyword):
    # URL encode the keyword to handle spaces and special characters
    encoded_keyword = quote(keyword.replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_keyword}"
    
    # Wikipedia API requires a User-Agent header
    headers = {
        'User-Agent': 'WikiFetcher/1.0 (https://example.com/contact)'
    }
    
    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()  # Raise an exception for bad status codes
        
        # Try to parse JSON
        data = resp.json()
        
        # TODO: Extract the 'extract' field safely
        # If missing, return some fallback text
        summary = data.get("extract", "No summary found.")
        return summary
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {str(e)}"
    except ValueError as e:
        return f"Error parsing response: {str(e)}"

def save_to_file(keyword, text):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{keyword}_{timestamp}.txt"

    # TODO: Write text to file
    # Use 'with open(filename, "w") as f'
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(text))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wiki_fetcher.py <keyword>")
        sys.exit(1)

    keyword = sys.argv[1]

    summary = fetch_summary(keyword)
    save_to_file(keyword, summary)
    print(f"Saved summary for {keyword}.")
