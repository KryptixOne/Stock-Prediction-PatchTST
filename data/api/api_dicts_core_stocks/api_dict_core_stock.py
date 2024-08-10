"""
Core Functions:

TIME_SERIES_INTRADAY: Provides intraday time series data (open, high, low, close, volume) for the specified equity, at intervals like 1, 5, 15, 30, or 60 minutes.
TIME_SERIES_DAILY: Returns daily time series data for the specified equity.
TIME_SERIES_DAILY_ADJUSTED: Similar to TIME_SERIES_DAILY, but includes adjusted close prices for dividends and splits.
TIME_SERIES_WEEKLY: Provides weekly time series data.
TIME_SERIES_WEEKLY_ADJUSTED: Similar to TIME_SERIES_WEEKLY, but includes adjusted prices.
TIME_SERIES_MONTHLY: Provides monthly time series data.
TIME_SERIES_MONTHLY_ADJUSTED: Similar to TIME_SERIES_MONTHLY, but includes adjusted prices.
GLOBAL_QUOTE: Returns the latest price and trading information for a single stock.
SYMBOL_SEARCH: Allows searching for stocks and ETFs that match keywords (like "Tesla") and provides relevant symbol information.


"""


api_key=None
symbol=None
# 1. TIME_SERIES_INTRADAY
api_dict_INTRADAY = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': symbol,
    'interval': '5min',  # Supported intervals: 1min, 5min, 15min, 30min, 60min
    'apikey': api_key,
    'outputsize': 'compact',  # Optional; default is 'compact', can be 'full'
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 2. TIME_SERIES_DAILY
api_dict_DAILY = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': symbol,
    'apikey': api_key,
    'outputsize': 'compact',  # Optional; default is 'compact', can be 'full'
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 3. TIME_SERIES_DAILY_ADJUSTED
api_dict_DAILY_ADJUSTED = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': symbol,
    'apikey': api_key,
    'outputsize': 'compact',  # Optional; default is 'compact', can be 'full'
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 4. TIME_SERIES_WEEKLY
api_dict_WEEKLY = {
    'function': 'TIME_SERIES_WEEKLY',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 5. TIME_SERIES_WEEKLY_ADJUSTED
api_dict_WEEKLY_ADJUSTED = {
    'function': 'TIME_SERIES_WEEKLY_ADJUSTED',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 6. TIME_SERIES_MONTHLY
api_dict_MONTHLY = {
    'function': 'TIME_SERIES_MONTHLY',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 7. TIME_SERIES_MONTHLY_ADJUSTED
api_dict_MONTHLY_ADJUSTED = {
    'function': 'TIME_SERIES_MONTHLY_ADJUSTED',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 8. GLOBAL_QUOTE
api_dict_GLOBAL_QUOTE = {
    'function': 'GLOBAL_QUOTE',
    'symbol': symbol,
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}

# 9. SYMBOL_SEARCH
api_dict_SYMBOL_SEARCH = {
    'function': 'SYMBOL_SEARCH',
    'keywords': 'Tesla',  # Example; can be any keyword
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is 'json', can be 'csv'
}
