from data.api.api_dicts_technical import api_dict_cycle,api_dict_volume,api_dicts_volatility,api_dicts_ocillators,\
    api_dicts_moving_averages
from data.api.api_dicts_economic import api_dicts_economics
from data.api.api_dicts_core_stocks import api_dict_core_stock



economic_data_functions = [
        api_dicts_economics.api_dict_GDP,
        api_dicts_economics.api_dict_GDP_PER_CAPITA,
        api_dicts_economics.api_dict_TREASURY_YIELD,
        api_dicts_economics.api_dict_FED_FUNDS_RATE,
        api_dicts_economics.api_dict_CPI,
        api_dicts_economics.api_dict_INFLATION,
        api_dicts_economics.api_dict_RETAIL_SALES,
        api_dicts_economics.api_dict_DURABLE_GOODS,
        api_dicts_economics.api_dict_UNEMPLOYMENT,
        api_dicts_economics.api_dict_NONFARM_PAYROLL
]
technical_cycle_functions = [
        api_dict_cycle.api_dict_HT_DCPERIOD,
        api_dict_cycle.api_dict_HT_DCPHASE,
        api_dict_cycle.api_dict_HT_PHASOR,
        api_dict_cycle.api_dict_HT_SINE,
        api_dict_cycle.api_dict_HT_TRENDLINE,
        api_dict_cycle.api_dict_HT_TRENDMODE
]

technical_volume_functions = [
        api_dict_volume.api_dict_AD,
        api_dict_volume.api_dict_ADOSC,
        api_dict_volume.api_dict_CMF,
        api_dict_volume.api_dict_OBV
]

technical_volatility_functions = [
        api_dicts_volatility.api_dict_ATR,
        api_dicts_volatility.api_dict_BBANDS,
        api_dicts_volatility.api_dict_NATR,
        api_dicts_volatility.api_dict_TRANGE
]

technical_oscillators_functions = [
        api_dicts_ocillators.api_dict_ADX,
        api_dicts_ocillators.api_dict_ADXR,
        api_dicts_ocillators.api_dict_APO,
        api_dicts_ocillators.api_dict_AROON,
        api_dicts_ocillators.api_dict_AROONOSC,
        api_dicts_ocillators.api_dict_CCI,
        api_dicts_ocillators.api_dict_DX,
        api_dicts_ocillators.api_dict_,
        api_dicts_ocillators.MACD,
        api_dicts_ocillators.api_dict_MACDEXT,
        api_dicts_ocillators.api_dict_MFI,
        api_dicts_ocillators.api_dict_MINUS_DI,
        api_dicts_ocillators.api_dict_MINUS_DM,
        api_dicts_ocillators.api_dict_MOM,
        api_dicts_ocillators.api_dict_PLUS_DI,
        api_dicts_ocillators.api_dict_PLUS_DM,
        api_dicts_ocillators.api_dict_PPO,
        api_dicts_ocillators.api_dict_ROC,
        api_dicts_ocillators.api_dict_ROCR,
        api_dicts_ocillators.api_dict_RSI,
        api_dicts_ocillators.api_dict_STOCH,
        api_dicts_ocillators.api_dict_STOCHRSI,
        api_dicts_ocillators.api_dict_TRIX,
        api_dicts_ocillators.api_dict_ULTOSC,
        api_dicts_ocillators.api_dict_WILLR
]

technical_moving_avg_functions = [
        api_dicts_moving_averages.api_dict_DEMA,
        api_dicts_moving_averages.api_dict_EMA,
        api_dicts_moving_averages.api_dict_KAMA,
        api_dicts_moving_averages.api_dict_MAMA,
        api_dicts_moving_averages.api_dict_SMA,
        api_dicts_moving_averages.api_dict_T3,
        api_dicts_moving_averages.api_dict_TEMA,
        api_dicts_moving_averages.api_dict_TRIMA,
        api_dicts_moving_averages.api_dict_WMA
]

core_stock_functions = [
        api_dict_core_stock.api_dict_DAILY,
        api_dict_core_stock.api_dict_DAILY_ADJUSTED,
        api_dict_core_stock.api_dict_GLOBAL_QUOTE,
        api_dict_core_stock.api_dict_INTRADAY,
        api_dict_core_stock.api_dict_MONTHLY,
        api_dict_core_stock.api_dict_MONTHLY_ADJUSTED,
        api_dict_core_stock.api_dict_SYMBOL_SEARCH,
        api_dict_core_stock.api_dict_WEEKLY,
        api_dict_core_stock.api_dict_WEEKLY_ADJUSTED
]