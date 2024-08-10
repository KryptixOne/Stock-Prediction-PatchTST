"""
Moving Averages: SMA, EMA, WMA, DEMA, TEMA, TRIMA, KAMA, MAMA, T3
"""
symbol = None
api_key = None

## Moving averages:

# 1. Simple Moving Average (SMA)
api_dict_SMA = {
    'function': 'SMA',
    'symbol': symbol,
    'interval': 'daily',  # Supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    'apikey': api_key,
    'time_period': 20,  # Example value; can be any positive integer
    'series_type': 'close',  # close, open, high, low
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 2. Exponential Moving Average (EMA)
api_dict_EMA = {
    'function': 'EMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 3. Weighted Moving Average (WMA)
api_dict_WMA = {
    'function': 'WMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 4. Double Exponential Moving Average (DEMA)
api_dict_DEMA = {
    'function': 'DEMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 5. Triple Exponential Moving Average (TEMA)
api_dict_TEMA = {
    'function': 'TEMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 6. Triangular Moving Average (TRIMA)
api_dict_TRIMA = {
    'function': 'TRIMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 7. Kaufman Adaptive Moving Average (KAMA)
api_dict_KAMA = {
    'function': 'KAMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}

# 8. MESA Adaptive Moving Average (MAMA)
api_dict_MAMA = {
    'function': 'MAMA',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'fastlimit': 0.01,  # Optional; default is 0.01
    'slowlimit': 0.01,  # Optional; default is 0.01
    'datatype': 'json',
}

# 9. T3 Moving Average (T3)
api_dict_T3 = {
    'function': 'T3',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'series_type': 'close',
    'datatype': 'json',
}


