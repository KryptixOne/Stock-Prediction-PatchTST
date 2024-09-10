import requests
from bs4 import BeautifulSoup
import time

url_dictionary = {
    'Technology': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology/',
    'Financial_Services': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_financial-services/',
    'Healthcare': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_healthcare/',
    'Consumer_Cyclical': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-cyclical/',
    'Industrials': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_industrials/',
    'Communication_Services': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_communication-services/',
    'Consumer_Defensive': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-defensive/',
    'Energy': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_energy/',
    'Real_Estate': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate/',
    'Basic_Materials': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_basic-materials/',
    'Utilities': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_utilities/'
    }


# Function to scrape symbols from a specific offset page
def get_stock_symbols(offset, url):
    offset_update = f'?count=25&offset={offset}'
    url = url + offset_update
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

import requests
from bs4 import BeautifulSoup
import time
import json

# Dictionary containing sector URLs
url_dictionary = {
    'Technology': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_technology/',
    'Financial_Services': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_financial-services/',
    'Healthcare': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_healthcare/',
    'Consumer_Cyclical': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-cyclical/',
    'Industrials': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_industrials/',
    'Communication_Services': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_communication-services/',
    'Consumer_Defensive': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_consumer-defensive/',
    'Energy': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_energy/',
    'Real_Estate': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_real-estate/',
    'Basic_Materials': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_basic-materials/',
    'Utilities': 'https://finance.yahoo.com/screener/predefined/sec-ind_sec-largest-equities_utilities/'
}

# Function to save the sector symbols dictionary to a JSON file
def save_dictionary_to_json(dictionary, filename="sector_symbols.json"):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)
    print(f"Dictionary saved to {filename}")


# Function to scrape symbols from a specific offset page
def get_stock_symbols(offset, url):
    offset_update = f'?count=25&offset={offset}'
    url = url + offset_update
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


# Function to loop through multiple pages and collect stock symbols for a sector
def scrape_multiple_pages(url, max_pages=5):
    all_symbols = []
    for page in range(max_pages):
        offset = page * 25  # Calculate offset for each page
        symbols = get_stock_symbols(offset, url)
        if not symbols:  # Break the loop if no symbols are returned (end of pages)
            break
        all_symbols.extend(symbols)
        print(f"Page {page + 1}: {symbols}")
        time.sleep(1)  # Adding a delay to avoid being blocked
    return all_symbols


# Main function to scrape all sectors
def scrape_all_sectors(max_pages_per_sector=5):
    sector_symbols = {}
    for sector, url in url_dictionary.items():
        print(f"Scraping sector: {sector}")
        symbols = scrape_multiple_pages(url, max_pages=max_pages_per_sector)
        sector_symbols[sector] = symbols
        print(f"Total symbols for {sector}: {len(symbols)}")
    return sector_symbols


# Scrape all sectors with a limit of 5 pages per sector (adjust max_pages_per_sector as needed)
all_sector_symbols = scrape_all_sectors(50)

# Print the total number of symbols scraped per sector
for sector, symbols in all_sector_symbols.items():
    print(f"{sector}: {len(symbols)} symbols")


# Save the result to a JSON file
save_dictionary_to_json(all_sector_symbols, "sector_symbols.json")
