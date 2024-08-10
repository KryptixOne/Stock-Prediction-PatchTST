"""Cycle Indictators: OBV, AD, ADOSC, CMF"""


symbol = None
api_key=None

# 1. Hilbert Transform - Instantaneous Trendline (HT_TRENDLINE)
api_dict_HT_TRENDLINE = {
    'function': 'HT_TRENDLINE',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}

# 2. Hilbert Transform - Sinewave (HT_SINE)
api_dict_HT_SINE = {
    'function': 'HT_SINE',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}

# 3. Hilbert Transform - Trend vs Cycle Mode (HT_TRENDMODE)
api_dict_HT_TRENDMODE = {
    'function': 'HT_TRENDMODE',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}

# 4. Hilbert Transform - Dominant Cycle Period (HT_DCPERIOD)
api_dict_HT_DCPERIOD = {
    'function': 'HT_DCPERIOD',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}

# 5. Hilbert Transform - Dominant Cycle Phase (HT_DCPHASE)
api_dict_HT_DCPHASE = {
    'function': 'HT_DCPHASE',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}

# 6. Hilbert Transform - Phasor Components (HT_PHASOR)
api_dict_HT_PHASOR = {
    'function': 'HT_PHASOR',
    'symbol': symbol,
    'interval': 'daily',
    'apikey': api_key,
    'series_type': 'close',
    'datatype': 'json',
}
