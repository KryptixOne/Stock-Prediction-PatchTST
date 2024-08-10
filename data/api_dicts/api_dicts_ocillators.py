"""Oscillators: RSI, STOCH, MACD, MACDEXT, STOCHRSI, WILLR, ADX, ADXR,
            APO, PPO, MOM, CCI, ROC, ROCR, AROON, AROONOSC, MFI, TRIX,
             ULTOSC, DX, MINUS_DI, PLUS_DI, MINUS_DM, PLUS_DM

"""
symbol = None
api_key = None
# 1. Relative Strength Index (RSI)
api_dict_RSI = {
    'function': 'RSI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,  # Example value
    'series_type': 'close',
    'datatype': 'json',
}

# 2. Stochastic Oscillator (STOCH)
api_dict_STOCH = {
    'function': 'STOCH',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'fastkperiod': 5,
    'slowkperiod': 3,
    'slowdperiod': 3,
    'slowkmatype': 0,  # SMA
    'slowdmatype': 0,  # SMA
    'datatype': 'json',
}

# 3. Moving Average Convergence Divergence (MACD)
api_dict_MACD = {
    'function': 'MACD',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'fastperiod': 12,  # Default value
    'slowperiod': 26,  # Default value
    'signalperiod': 9,  # Default value
    'datatype': 'json',
}

# 4. MACD with Controllable Moving Average (MACDEXT)
api_dict_MACDEXT = {
    'function': 'MACDEXT',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'fastperiod': 12,
    'slowperiod': 26,
    'signalperiod': 9,
    'fastmatype': 0,  # SMA
    'slowmatype': 0,  # SMA
    'signalmatype': 0,  # SMA
    'datatype': 'json',
}

# 5. Stochastic Relative Strength Index (STOCHRSI)
api_dict_STOCHRSI = {
    'function': 'STOCHRSI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'series_type': 'close',
    'fastkperiod': 5,  # Default value
    'fastdperiod': 3,  # Default value
    'fastdmatype': 0,  # SMA
    'datatype': 'json',
}

# 6. Williams %R (WILLR)
api_dict_WILLR = {
    'function': 'WILLR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,  # Example value
    'datatype': 'json',
}

# 7. Average Directional Movement Index (ADX)
api_dict_ADX = {
    'function': 'ADX',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 8. Average Directional Movement Index Rating (ADXR)
api_dict_ADXR = {
    'function': 'ADXR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 9. Absolute Price Oscillator (APO)
api_dict_APO = {
    'function': 'APO',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'fastperiod': 12,
    'slowperiod': 26,
    'matype': 0,  # SMA
    'datatype': 'json',
}

# 10. Percentage Price Oscillator (PPO)
api_dict_PPO = {
    'function': 'PPO',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'fastperiod': 12,
    'slowperiod': 26,
    'matype': 0,  # SMA
    'datatype': 'json',
}

# 11. Momentum (MOM)
api_dict_MOM = {
    'function': 'MOM',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 10,
    'series_type': 'close',
    'datatype': 'json',
}

# 12. Commodity Channel Index (CCI)
api_dict_CCI = {
    'function': 'CCI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,
    'datatype': 'json',
}

# 13. Rate of Change (ROC)
api_dict_ROC = {
    'function': 'ROC',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 10,
    'series_type': 'close',
    'datatype': 'json',
}

# 14. Rate of Change Ratio (ROCR)
api_dict_ROCR = {
    'function': 'ROCR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 10,
    'series_type': 'close',
    'datatype': 'json',
}

# 15. Aroon (AROON)
api_dict_AROON = {
    'function': 'AROON',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 16. Aroon Oscillator (AROONOSC)
api_dict_AROONOSC = {
    'function': 'AROONOSC',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 17. Money Flow Index (MFI)
api_dict_MFI = {
    'function': 'MFI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 18. TRIX (TRIX)
api_dict_TRIX = {
    'function': 'TRIX',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 15,
    'series_type': 'close',
    'datatype': 'json',
}

# 19. Ultimate Oscillator (ULTOSC)
api_dict_ULTOSC = {
    'function': 'ULTOSC',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'timeperiod1': 7,
    'timeperiod2': 14,
    'timeperiod3': 28,
    'datatype': 'json',
}

# 20. Directional Movement Index (DX)
api_dict_DX = {
    'function': 'DX',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 21. Minus Directional Indicator (MINUS_DI)
api_dict_MINUS_DI = {
    'function': 'MINUS_DI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 22. Plus Directional Indicator (PLUS_DI)
api_dict_PLUS_DI = {
    'function': 'PLUS_DI',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 23. Minus Directional Movement (MINUS_DM)
api_dict_MINUS_DM = {
    'function': 'MINUS_DM',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}

# 24. Plus Directional Movement (PLUS_DM)
api_dict_PLUS_DM = {
    'function': 'PLUS_DM',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 14,
    'datatype': 'json',
}
