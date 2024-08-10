import pandas as pd
import requests
import json


def build_api_url(api_dict):
    base_url = 'https://www.alphavantage.co/query?'
    for key, val in api_dict.items():
        base_url += f'{key}={val}&'
    return base_url[:-1]


def get_time_series_data(request_url):
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
