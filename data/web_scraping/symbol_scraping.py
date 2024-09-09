import requests
from bs4 import BeautifulSoup
import time


# Function to scrape symbols from a specific offset page
def get_stock_symbols(offset):
    url = f'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology/?count=25&offset={offset}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Sending request with the user-agent header
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error {response.status_code}: Unable to retrieve page with offset {offset}.")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all stock symbols on the page
    symbols = [tag.text for tag in soup.find_all('a', attrs={'data-test': 'quoteLink'})]

    return symbols


# Function to loop through multiple pages and collect stock symbols
def scrape_multiple_pages(max_pages):
    all_symbols = []
    for page in range(max_pages):
        offset = page * 25  # Calculate offset for each page: page 1 -> offset 0, page 2 -> offset 25, etc.
        symbols = get_stock_symbols(offset)
        if not symbols:  # Break the loop if no symbols are returned
            break
        all_symbols.extend(symbols)
        print(f"Page {page + 1}: {symbols}")
        time.sleep(2)  # Adding a delay to avoid being blocked
    return all_symbols


# Scrape the first 5 pages (adjust the number as needed)
all_symbols = scrape_multiple_pages(5)
print(f"Total symbols scraped: {len(all_symbols)}")
