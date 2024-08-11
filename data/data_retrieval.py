"""retrieval of data"""
import requests
import numpy
import pandas as pd
import json
from data.api import economic_data_functions,technical_volume_functions, technical_cycle_functions, \
                        technical_oscillators_functions, technical_volatility_functions, \
                        technical_moving_avg_functions, core_stock_functions


def build_api_url(api_dict):
    base_url = 'https://www.alphavantage.co/query?'
    for key, val in api_dict.items():
        base_url += f'{key}={val}&'
    return base_url[:-1]

def send_get_url_request(request_url):
    response = requests.get(request_url)
    return response.json()

def convert_to_dataframe(time_series_data):
    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={
        'index': 'timestamp',
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    }, inplace=True)
    return df

def save_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)

def get_economic_data(list_of_api_functions, api_key):
    ...

def get_technical_data(list_of_technical_functions, symbol, api_key):
    ...

def get_core_stock_data(list_of_core_stock_functions, symbol, api_key):
    ...

if __name__ == '__main__':
    # Symbols, API Key, etc
    api_key = 'P6PNGBDDG24IDFDV'
    symbols = [
        "SPY", "QQQ", "DIA", "IWM", "VIXY", "EFA", "EWJ",  # Market Indices (ETFs)
        "TSLA", "AMZN", "NVDA", "GME", "AMD", "BABA",  # High Volatility Stocks
        "AAPL", "MSFT", "GOOGL", "FB", "NFLX", "BA", "XOM",  # Medium Volatility Stocks
        "JNJ", "KO", "PG", "PEP", "T", "VZ",  # Low Volatility Stocks
        "EWW", "EWZ", "ASHR", "EWG",  # Global Exposure
        "USO", "GLD", "SLV", "DBA",  # Commodities
        "MU", "BYND", "PLTR", "RIVN",  # Very High Volatility Stocks
        "VXX",  # iPath Series B S&P 500 VIX Short-Term Futures ETN (Volatility)
        "UVXY",  # ProShares Ultra VIX Short-Term Futures ETF (Volatility)
        "SVXY",  # ProShares Short VIX Short-Term Futures ETF (Inverse Volatility)
        "VIX"  # CBOE Volatility Index (Volatility Index)
    ]


