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
import os


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
    df.rename(columns=rename_dict, inplace=True)
    # Convert 'timestamp' to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Convert available columns to numeric
    columns_to_convert = list(df.columns)
    columns_to_convert.remove('timestamp')
    existing_columns = [col for col in columns_to_convert if col in df.columns]

    df[existing_columns] = df[existing_columns].apply(pd.to_numeric)

    return df


def convert_econdata_to_dataframe(data_in, function_name: str = ''):
    """
    Converts single econ_data format to dataframe:

    :param data_in: econ_data = output['CPI']['data']
    :param function_name: string name of Economic Data.
    :return: df
    """

    df = pd.DataFrame(data_in)
    rename_dict = {'value': function_name + '_value',
                   'date': 'timestamp'}
    df.rename(columns=rename_dict, inplace=True)
    print(df.head())
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    columns_to_convert = list(df.columns)
    columns_to_convert.remove('timestamp')
    existing_columns = [col for col in columns_to_convert if col in df.columns]

    df[existing_columns] = df[existing_columns].apply(pd.to_numeric)
    return df


def build_complete_econ_dataframe(all_econ_data):
    """
    Build a completely formatted economic data specific dataframe
    :param all_econ_data: Dictionary of All Economic data obtained from the API Ping
    :return: Dataframe of formatted economic data
    """
    econ_functions = list(all_econ_data.keys())
    complete_df = None
    for x in econ_functions:
        df = convert_econdata_to_dataframe(all_econ_data[x]['data'],
                                           function_name=x)
        if not isinstance(complete_df, pd.DataFrame):
            complete_df = df
        else:
            complete_df = complete_df.merge(df, on='timestamp', how='outer')
            complete_df = complete_df.sort_values(by='timestamp').ffill()

        for col in complete_df.columns:
            if col != 'timestamp':
                complete_df[col] = complete_df[col].astype(float)

        columns_to_convert = list(complete_df.columns)
        columns_to_convert.remove('timestamp')
        existing_columns = [col for col in columns_to_convert if col in complete_df.columns]

        complete_df[existing_columns] = complete_df[existing_columns].apply(pd.to_numeric)

    return complete_df


def build_complete_technical_dataframe(all_technical_data):
    """
    create the complete, individual symbol, technical data
    :param all_technical_data: all pricing and technical data, in dictionary format
    :return: The complete formatted dataframe:
    """
    tech_functions = list(all_technical_data.keys())
    complete_df = None
    for x in tech_functions:
        assert isinstance(all_technical_data[x], dict), (f'Datatype not expected. expected Dict,'
                                                         f' got {type(all_technical_data[x])} ')
        cur_keys = list(all_technical_data[x].keys())
        # Expected keys ['Meta_Data', Function Name]
        if 'Information' in cur_keys:
            print('Api limit reached, continuing')
            continue

        assert len(cur_keys) == 2, f'Expected number of keys is 2. Got {len(cur_keys)}'

        df = convert_to_dataframe(all_technical_data[x][cur_keys[1]])

        if not isinstance(complete_df, pd.DataFrame):
            complete_df = df
        else:
            complete_df = complete_df.merge(df, on='timestamp', how='outer')
            complete_df = complete_df.sort_values(by='timestamp').ffill()

        for col in complete_df.columns:
            if col != 'timestamp':
                complete_df[col] = complete_df[col].astype(float)

        columns_to_convert = list(complete_df.columns)
        columns_to_convert.remove('timestamp')
        existing_columns = [col for col in columns_to_convert if col in complete_df.columns]

        # Ensures that the columns are numeric.
        complete_df[existing_columns] = complete_df[existing_columns].apply(pd.to_numeric)

    return complete_df


def get_data(list_of_api_functions):
    """
    Function to acquire data via API ping
    :param list_of_api_functions: lsit of api functions
    :return: api information
    """
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


def save_dataframe_as_csv(df, save_dir, category, symbol):
    save_path = os.path.join(save_dir, category)
    os.makedirs(save_path, exist_ok=True)
    save_path_name = os.path.join(save_path, f'{symbol}_Price_Technical.csv')
    df.to_csv(save_path_name)
    return None

if __name__ == '__main__':
    """
    Notes on time_period_list choice:
    
    Intraday (1-minute, 5-minute, 15-minute, 30-minute, 1-hour):
    Day Trading: These short time frames are used by day traders who open and close positions within the same trading 
    day.They focus on very short-term price movements and rely heavily on technical analysis for quick decision-making.
    
    Short-Term (1-day, 2-day, 5-day, 15-day):
    Swing Trading: Swing traders hold positions for several days or weeks. They use short-term technical analysis to 
    capture price swings within a trend.
    
    Medium-Term (1-month, 3-month, 6-month):
    Position Trading: Position traders have a longer-term perspective and may hold positions for several months. They
    use medium-term technical analysis to make decisions on trend direction and entry/exit points.
    
    Long-Term (1-year, 3-year, 5-year, 10-year):
    Investing: Long-term investors, such as buy-and-hold investors, use technical analysis to analyze the overall health
    of a stock, identify potential entry points, and determine the best times to rebalance or exit long-term positions.

    """

    # Symbols and API Key
    save_dir = './raw_data'
    update_econ_data = True
    obtain_technical_data = False

    # Time period for technical analysis to take into consideration.
    time_period = 15

    # Get API and symbol/sector info.
    api_key = api_key.api_key
    symbol_dict = symbol_list.symbol_dict
    sector_list = symbol_list.sector_list
    # Get Historical Info per symbol:
    function_groups = [
        economic_data_functions,
        technical_volume_functions,
        technical_cycle_functions,
        technical_oscillators_functions,
        technical_volatility_functions,
        technical_moving_avg_functions
    ]

    econ_data = None
    for category, sectors in symbol_dict.items():
        for sector, symbols in sectors.items():
            for symbol in symbols:
                # Update Symbol based functions
                for functions in function_groups:
                    for function in functions:
                        all_keys = list(function.keys())
                        function['symbol'] = symbol
                        function['apikey'] = api_key
                        if 'time_period' in all_keys:
                            function['time_period'] = time_period

                # Get base price info
                api_dict_WEEKLY_ADJUSTED['symbol'] = symbol
                api_dict_WEEKLY_ADJUSTED['apikey'] = api_key
                input_list_core = [api_dict_WEEKLY_ADJUSTED]
                output = get_data(input_list_core)

                # Get Econ Data Once to prevent pinging API too many times.
                if update_econ_data:
                    econ_data = get_data(economic_data_functions)
                    econ_data_formatted = build_complete_econ_dataframe(econ_data)
                    econ_dir = os.path.join(save_dir,'Economic_Data')
                    os.makedirs(econ_dir, exist_ok=True)
                    econ_data_formatted.to_csv(os.path.join(econ_dir ,'Economic_data_historical.csv'))
                    # Remove data for memory efficiency
                    del econ_data
                    del econ_data_formatted
                    update_econ_data = False

                all_tech_indicators = [
                    technical_moving_avg_functions,
                    technical_volatility_functions,
                    technical_cycle_functions,
                    technical_oscillators_functions,
                    technical_volume_functions
                ]
                if obtain_technical_data:
                    for indicators in all_tech_indicators:
                        output.update(get_data(indicators))

                        # Put a wait timer here. To prevent Overloading API.
                        # timer.pause()
                        # Depending on API Key level (max_pings per min)/60 = wait timer

                completed_technical_df = build_complete_technical_dataframe(output)
                assert completed_technical_df is not None, ('Output dataframe is NoneType. Check that api limit is not '
                                                            'reached')
                completed_technical_df['sector'] = sector_list.index(sector)
                # Save Csv
                save_dataframe_as_csv(df=completed_technical_df, save_dir=save_dir,
                                      category=category, symbol=symbol)

                print(f'Acquired information for {symbol} in {category} - {sector}')
