"""Economic Data:
REAL_GDP: Measures the total value of all goods and services produced in a country, adjusted for inflation.
REAL_GDP_PER_CAPITA: GDP divided by the population, giving an average economic output per person.
TREASURY_YIELD: The return on U.S. government debt securities of varying maturities.
FEDERAL_FUNDS_RATE: The interest rate at which banks lend to each other overnight.
CPI: A measure of the average change in prices paid by consumers for goods and services.
INFLATION: The annual percentage increase in the CPI, reflecting the rise in prices.
RETAIL_SALES: Total sales by retail stores, an indicator of consumer demand.
DURABLE_GOODS: Orders for goods expected to last at least three years, indicating future manufacturing activity.
UNEMPLOYMENT: The percentage of the labor force that is jobless and actively seeking employment.
NONFARM_PAYROLL: The total number of paid U.S. workers excluding farm employees, government workers, and non-profit employees, indicating overall economic health.
"""


api_key=None
# 1. Real GDP
api_dict_GDP = {
    'function': 'REAL_GDP',
    'interval': 'annual',  # Supported intervals: annual, quarterly
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 2. Real GDP per Capita
api_dict_GDP_PER_CAPITA = {
    'function': 'REAL_GDP_PER_CAPITA',
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 3. Treasury Yield
api_dict_TREASURY_YIELD = {
    'function': 'TREASURY_YIELD',
    'interval': 'weekly',  # Supported intervals: daily, weekly, monthly
    'maturity': '10year',  # Supported maturities: 3month, 2year, 5year, 7year, 10year, 30year
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 4. Federal Funds Rate
api_dict_FED_FUNDS_RATE = {
    'function': 'FEDERAL_FUNDS_RATE',
    'interval': 'weekly',  # Supported intervals: daily, weekly, monthly, annual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 5. Consumer Price Index (CPI)
api_dict_CPI = {
    'function': 'CPI',
    'interval': 'monthly',  # Supported intervals: monthly, semiannual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 6. Inflation
api_dict_INFLATION = {
    'function': 'INFLATION',
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 7. Retail Sales
api_dict_RETAIL_SALES = {
    'function': 'RETAIL_SALES',
    'interval': 'monthly',  # Supported intervals: monthly, annual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 8. Durable Goods Orders
api_dict_DURABLE_GOODS = {
    'function': 'DURABLE_GOODS',
    'interval': 'monthly',  # Supported intervals: monthly, annual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 9. Unemployment Rate
api_dict_UNEMPLOYMENT = {
    'function': 'UNEMPLOYMENT',
    'interval': 'monthly',  # Supported intervals: monthly, annual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}

# 10. Nonfarm Payroll
api_dict_NONFARM_PAYROLL = {
    'function': 'NONFARM_PAYROLL',
    'interval': 'monthly',  # Supported intervals: monthly, annual
    'apikey': api_key,
    'datatype': 'json',  # Optional; default is json, can be 'json' or 'csv'
}
