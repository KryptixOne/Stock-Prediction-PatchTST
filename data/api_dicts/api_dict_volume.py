""" Volume Indicators: OBV, AD, ADOSC, CMF"""

symbol = None
api_key=None
# 1. On-Balance Volume (OBV)
api_dict_OBV = {
    'function': 'OBV',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'datatype': 'json',
}

# 2. Chaikin A/D Line (AD)
api_dict_AD = {
    'function': 'AD',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'datatype': 'json',
}

# 3. Chaikin A/D Oscillator (ADOSC)
api_dict_ADOSC = {
    'function': 'ADOSC',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'fastperiod': 3,  # Example value; default is 3
    'slowperiod': 10,  # Example value; default is 10
    'datatype': 'json',
}

# 4. Chaikin Money Flow (CMF)
api_dict_CMF = {
    'function': 'CMF',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'time_period': 20,  # Example value
    'datatype': 'json',
}
