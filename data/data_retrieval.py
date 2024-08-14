"""retrieval of data"""
import requests
import numpy
import pandas as pd
import json
from data.api import economic_data_functions, technical_volume_functions, technical_cycle_functions, \
    technical_oscillators_functions, technical_volatility_functions, \
    technical_moving_avg_functions
from data.api.api_dicts_core_stocks.api_dict_core_stock import api_dict_DAILY_ADJUSTED, api_dict_WEEKLY_ADJUSTED
from data.api import symbol_list, api_key

def build_api_url(api_dict):
    base_url = 'https://www.alphavantage.co/query?'
    for key, val in api_dict.items():
        base_url += f'{key}={val}&'
    return base_url[:-1]


def send_get_url_request(request_url):
    response = requests.get(request_url)
    return response.json()


def combine_data(json_data):
    dfs = {}
    for symbol, datasets in json_data.items():
        # Convert time_series_data1
        time_series_df = pd.DataFrame.from_dict(datasets['time_series_data1'], orient='index')
        # Convert technical_indicator_data
        technical_df = pd.DataFrame.from_dict(datasets['technical_indicator_data'], orient='index')
        # Combine both DataFrames
        combined_df = time_series_df.join(technical_df)
        dfs[symbol] = combined_df

    # Example of accessing the DataFrame for a particular symbol
    print(dfs.head())


def convert_to_dataframe(time_series_data):
    """
    For time series pricing data. comes out as a different format from this crap
    :param time_series_data: output['Weekly Adjusted Time Series']
    :return: dataframe
    """

    df = pd.DataFrame.from_dict(time_series_data, orient='index')
    df.reset_index(inplace=True)
    rename_dict = {'index': 'timestamp'}
    # Convert 'timestamp' to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Convert available columns to numeric
    columns_to_convert = list(df.columns[1:])
    columns_to_convert.remove('timestamp')
    existing_columns = [col for col in columns_to_convert if col in df.columns]

    df[existing_columns] = df[existing_columns].apply(pd.to_numeric)

    return df


def convert_econdata_to_dataframe(econ_data):
    """
    Converts econ_data format to dataframe:

    :param econ_data: econ_data = output['CPI']['data']
    :return: df
    """

    df = pd.DataFrame(econ_data)
    df['date'] = pd.to_datetime(df['date'])
    return df


def save_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)


def get_data(list_of_api_functions):
    output_dict = {}
    for func in list_of_api_functions:
        if func['function'] == 'INFLATION':
            pass
        url = build_api_url(func)
        output_data = send_get_url_request(url)
        if 'data' in output_data:
            for k in range(len(output_data['data'])):
                cur_data = output_data['data'][k]
                if 'value' in cur_data:
                    # Convert the 'value' to a float and round it to 4 decimal places
                    cur_data['value'] = round(float(cur_data['value']), 4)

        output_dict[func['function']] = output_data
    return output_dict


if __name__ == '__main__':
    # Symbols and API Key


    api_key = api_key.api_key
    symbol_dict = symbol_list.symbol_dict
    # Get Historical Info per symbol:
    function_groups = [
        economic_data_functions,
        technical_volume_functions,
        technical_cycle_functions,
        technical_oscillators_functions,
        technical_volatility_functions,
        technical_moving_avg_functions
    ]

    for category, sectors in symbol_dict.items():
        for sector, symbols in sectors.items():
            for symbol in symbols:
                api_dict_WEEKLY_ADJUSTED['symbol'] = symbol
                api_dict_WEEKLY_ADJUSTED['apikey'] = api_key

                input_list_core = [api_dict_WEEKLY_ADJUSTED]
                output = get_data(input_list_core)

                output.update(get_data(economic_data_functions))

                # Update Symbol based functions
                for functions in function_groups:
                    for function in functions:
                        function['symbol'] = symbol
                        function['apikey'] = api_key

                all_tech_indicators = [
                    technical_moving_avg_functions,
                    technical_volatility_functions,
                    technical_cycle_functions,
                    technical_oscillators_functions,
                    technical_volume_functions
                ]
                for indicators in all_tech_indicators:
                    output.update(get_data(indicators))

                print(f'Acquired information for {symbol} in {category} - {sector}')
