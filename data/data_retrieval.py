"""retrieval of data"""
import requests
import numpy
import pandas as pd

from data.api import economic_data_functions,technical_volume_functions, technical_cycle_functions, \
                        technical_oscillators_functions, technical_volatility_functions, \
                        technical_moving_avg_functions, core_stock_functions


def get_economic_data(list_of_api_functions):
    ...


symbols = [
    "SPY", "QQQ", "DIA", "IWM", "VIXY", "EFA", "EWJ",  # Market Indices (ETFs)
    "TSLA", "AMZN", "NVDA", "GME", "AMD", "BABA",  # High Volatility Stocks
    "AAPL", "MSFT", "GOOGL", "FB", "NFLX", "BA", "XOM",  # Medium Volatility Stocks
    "JNJ", "KO", "PG", "PEP", "T", "VZ",  # Low Volatility Stocks
    "EWW", "EWZ", "ASHR", "EWG",  # Global Exposure
    "USO", "GLD", "SLV", "DBA",  # Commodities
    "MU",  # Micron Technology (High Volatility)
    "BYND",  # Beyond Meat, Inc. (High Volatility)
    "PLTR",  # Palantir Technologies Inc. (High Volatility)
    "RIVN"   # Rivian Automotive, Inc. (High Volatility)
]

api_key = 'P6PNGBDDG24IDFDV'
