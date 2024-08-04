
import pandas as pd
import requests
import json
# Replace with your actual Alpha Vantage API key
api_key = 'P6PNGBDDG24IDFDV'

api_dict = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'SPY',
    'apikey': 'P6PNGBDDG24IDFDV',
    'month':'2009-01',
    'outputsize':'full'
}
request_url_base = 'https://www.alphavantage.co/query?'

for key, val in api_dict.items():
    request_url_base = request_url_base+ key +'='+val + '&'
request_url_base = request_url_base[:-1]


r = requests.get(request_url_base)
data = r.json()
print(json.dumps(data, indent=4))

time_series_data = data['Time Series (Daily)']

# Convert to DataFrame
df = pd.DataFrame.from_dict(time_series_data, orient='index')

# Reset index to have date-time as a column
df.reset_index(inplace=True)

# Rename columns for better readability
df.rename(columns={
    'index': 'timestamp',
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. volume': 'volume'
}, inplace=True)

# Save to CSV
df.to_csv('SPY_Daily_Data.csv', index=False)

# Print the first few rows to verify
print(df)