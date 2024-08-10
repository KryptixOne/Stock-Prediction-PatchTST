from utils.alpha_vantage.historical_data_retrieval_price import build_api_url, get_time_series_data, \
    convert_to_dataframe, save_dataframe_to_csv


def main(api_key, symbol, output_filename):
    api_dict_daily_price = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'full'
    }
    api_dict_CPI = {
        'function': 'CPI',
        'apikey': api_key,
    }
    api_dict_INFLATION = {
        'function': 'INFLATION',
        'apikey': api_key,
        'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
    }
    api_dict_FEDERAL_FUNDS_RATE = {
        'function': 'FEDERAL_FUNDS_RATE',
        'apikey': api_key,
        'interval':'daily'
    }
    api_dict_RSI = {
        'function': 'RSI',
        'symbol': symbol,
        'interval':'weekly',  # following supported 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        'apikey': api_key,
        'time_period':10,  # Can be any value, 10-100
        'series_type':'close', # close, open, high, low
    }
    
    api_dict_BBANDS = {
        'function': 'BBANDS',
        'symbol': symbol,
        'interval': 'daily',  # Supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        'apikey': api_key,
        'time_period': 20,  # Example value; can be any positive integer
        'series_type': 'close',  # close, open, high, low
        'nbdevup': 2,  # Optional; default is 2
        'nbdevdn': 2,  # Optional; default is 2
        'matype': 0,  # Optional; default is 0 (Simple Moving Average), range 0-8
        'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
    }

    api_dict_EMA = {
        'function': 'EMA',
        'symbol': symbol,
        'interval': 'daily',  # Supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        'apikey': api_key,
        'time_period': 20,  # Example value; can be any positive integer
        'series_type': 'close',  # close, open, high, low
        'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
    }

    request_url = build_api_url(api_dict)
    data = get_time_series_data(request_url)
    time_series_data = data['Time Series (Daily)']

    df = convert_to_dataframe(time_series_data)
    save_dataframe_to_csv(df, output_filename)

    print(f"Data saved to {output_filename}")
    print(df.head())


# Example usage:
if __name__ == "__main__":
    api_key = 'P6PNGBDDG24IDFDV'
    symbol = 'SPY'
    output_filename = 'SPY_Daily_Data.csv'
    main(api_key, symbol, output_filename)
