""" Volatility Indicators: BBANDS, ATR, TRANGE, NATR"""
symbol = None
api_key = None

# 1. Bollinger Bands (BBANDS)
api_dict_BBANDS = {
    'function': 'BBANDS',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,  # Example value
    'series_type': 'close',
    'nbdevup': 2,  # Optional; default is 2
    'nbdevdn': 2,  # Optional; default is 2
    'matype': 0,  # Optional; default is 0 (SMA)
    'datatype': 'json',
}

# 2. Average True Range (ATR)
api_dict_ATR = {
    'function': 'ATR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,  # Example value
    'datatype': 'json',
}

# 3. True Range (TRANGE)
api_dict_TRANGE = {
    'function': 'TRANGE',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'datatype': 'json',
}

# 4. Normalized Average True Range (NATR)
api_dict_NATR = {
    'function': 'NATR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,  # Example value
    'datatype': 'json',
}
