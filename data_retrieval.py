from utils.alpha_vantage.historical_data_retrieval_price import build_api_url, get_time_series_data, \
    convert_to_dataframe, save_dataframe_to_csv


def main(api_key, symbol, output_filename):
    api_dict_daily_price = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'full'
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
