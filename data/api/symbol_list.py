"""
Company breakdown:

### Market Indices (ETFs):
- **SPY**: S&P 500 ETF, tracks the 500 largest U.S. companies.
- **QQQ**: Nasdaq-100 ETF, focuses on tech-heavy large-cap companies.
- **DIA**: Dow Jones Industrial Average ETF, tracks 30 major U.S. companies.
- **IWM**: Russell 2000 ETF, represents small-cap U.S. companies.
- **VIXY**: Short-Term Volatility ETF, tracks VIX futures.
- **EFA**: MSCI EAFE ETF, developed international markets excluding the U.S. and Canada.
- **EWJ**: MSCI Japan ETF, Japanese market.
- **XLK**: Technology Select Sector SPDR Fund.
- **SOXX**: iShares PHLX Semiconductor ETF.

### Very High Volatility Stocks:
- **MU**: Micron Technology, Inc., semiconductors.
- **PLTR**: Palantir Technologies, data analytics software.
- **TSM**: Taiwan Semiconductor Manufacturing Company.
- **NIO**: NIO Inc., electric vehicles.
- **RIVN**: Rivian Automotive, Inc., electric vehicles.
- **PDD**: Pinduoduo Inc., Chinese e-commerce.
- **RIG**: Transocean Ltd., offshore drilling.
- **CVX**: Chevron Corporation, oil and gas.
- **OXY**: Occidental Petroleum Corporation, oil and gas.
- **FANG**: Diamondback Energy, Inc., oil and gas.
- **VLO**: Valero Energy Corporation, oil refining.

### High Volatility Stocks:
- **TSLA**: Tesla, Inc., electric vehicles and energy.
- **AMZN**: Amazon.com, Inc., e-commerce and cloud computing.
- **NVDA**: NVIDIA Corporation, semiconductor technology.
- **GME**: GameStop Corp., retail gaming.
- **AMD**: Advanced Micro Devices, Inc., semiconductors.
- **BABA**: Alibaba Group, Chinese e-commerce.
- **SHOP**: Shopify Inc., e-commerce platform.
- **NIO**: NIO Inc., Chinese electric vehicles.
- **BYND**: Beyond Meat, Inc., plant-based meat substitutes.

### Medium Volatility Stocks:
- **AAPL**: Apple Inc., consumer electronics and software.
- **MSFT**: Microsoft Corporation, software and cloud computing.
- **GOOGL**: Alphabet Inc., Google and advertising.
- **FB**: Meta Platforms, Inc., social media and technology.
- **NFLX**: Netflix, Inc., streaming services.
- **BA**: The Boeing Company, aerospace and defense.
- **XOM**: Exxon Mobil Corporation, oil and gas.
- **CAT**: Caterpillar Inc., construction equipment.
- **LMT**: Lockheed Martin Corporation, aerospace and defense.
- **MMM**: 3M Company, industrial and consumer goods.
- **HON**: Honeywell International Inc., conglomerate.

### Low Volatility Stocks:
- **JNJ**: Johnson & Johnson, pharmaceuticals and consumer goods.
- **KO**: The Coca-Cola Company, beverages.
- **PG**: The Procter & Gamble Company, consumer goods.
- **PEP**: PepsiCo, Inc., beverages and snacks.
- **T**: AT&T Inc., telecommunications.
- **VZ**: Verizon Communications Inc., telecommunications.
- **PFE**: Pfizer Inc., pharmaceuticals.
- **MRK**: Merck & Co., Inc., pharmaceuticals.
- **ABBV**: AbbVie Inc., biopharmaceuticals.
- **BMY**: Bristol-Myers Squibb, pharmaceuticals.
- **NEE**: NextEra Energy, Inc., utilities.
- **DUK**: Duke Energy Corporation, utilities.
- **SO**: The Southern Company, utilities.
- **AEP**: American Electric Power, utilities.
- **D**: Dominion Energy, Inc., utilities.

### Global Exposure:
- **EWW**: iShares MSCI Mexico ETF, Mexican equities.
- **EWZ**: iShares MSCI Brazil ETF, Brazilian equities.
- **ASHR**: Xtrackers Harvest CSI 300 China A-Shares ETF.
- **EWG**: iShares MSCI Germany ETF.
- **VEA**: Vanguard FTSE Developed Markets ETF.
- **IXN**: iShares Global Tech ETF.
- **KWEB**: KraneShares CSI China Internet ETF.
- **QQQJ**: Invesco NASDAQ Next Gen 100 ETF.
- **ARKK**: ARK Innovation ETF.
- **XITK**: SPDR FactSet Innovative Technology ETF.

### Commodities:
- **USO**: United States Oil Fund LP, tracks the price of oil.
- **GLD**: SPDR Gold Trust, tracks the price of gold.
- **SLV**: iShares Silver Trust, tracks the price of silver.
- **PALL**: Aberdeen Standard Physical Palladium Shares ETF.
- **PLTM**: GraniteShares Platinum Trust.
- **IAU**: iShares Gold Trust.
- **CORN**: Teucrium Corn Fund.
- **WEAT**: Teucrium Wheat Fund.
- **SOYB**: Teucrium Soybean Fund.
- **COW**: iPath Series B Bloomberg Livestock Subindex ETN.


### Volatility Indices:
- **VXX**: iPath Series B S&P 500 VIX Short-Term Futures ETN, tracks VIX futures.
- **UVXY**: ProShares Ultra VIX Short-Term Futures ETF, leveraged VIX futures.
- **SVXY**: ProShares Short VIX Short-Term Futures ETF, inverse VIX futures.
- **VIX**: CBOE Volatility Index, measures market volatility.

"""

sector_list = ["Energy",
            "Materials",
            "Industrials",
            "Utilities",
            "Healthcare",
            "Financials",
            "Consumer Discretionary",
            "Consumer Staples",
            "Information Technology",
            "Communication Services",
            "Real Estate",
            "etf_symbols"]

symbol_dict = {
    'Market Indices (ETFs)': {
        'General': ["SPY", "QQQ", "DIA", "IWM", "VIXY", "EFA", "EWJ"],
        'Technology': ["XLK", "SOXX"],
        'Consumer Discretionary': ["XLY", "XRT"],
        'Energy': ["XLE", "XOP"],
        'Healthcare': ["XLV", "XBI"],
    },
    'Very High Volatility Stocks': {
        'Technology': ["MU", "PLTR", "TSM", "AMD", "NVDA"],
        'Consumer Discretionary': ["BYND", "RIVN", "TSLA", "NIO", "PDD"],
        'Energy': ["RIG", "CVX", "OXY", "FANG", "VLO"],
    },
    'High Volatility Stocks': {
        'Consumer Discretionary': ["TSLA", "AMZN", "GME", "NIO", "BYND"],
        'Technology': ["NVDA", "AMD", "BABA", "SHOP", "PLTR"],
        'Energy': ["RIG", "CVX", "OXY", "FANG", "VLO"],
    },
    'Medium Volatility Stocks': {
        'Technology': ["AAPL", "MSFT", "GOOGL", "FB", "NFLX"],
        'Industrials': ["BA", "CAT", "LMT", "MMM", "HON"],
        'Energy': ["XOM", "SLB", "HAL", "PSX", "COP"],
        'Consumer Staples': ["KO", "PG", "PEP", "WMT", "COST"],
    },
    'Low Volatility Stocks': {
        'Healthcare': ["JNJ", "PFE", "MRK", "ABBV", "BMY"],
        'Consumer Staples': ["KO", "PG", "PEP", "WMT", "COST"],
        'Communication Services': ["T", "VZ", "CHTR", "TMUS", "CMCSA"],
        'Utilities': ["NEE", "DUK", "SO", "AEP", "D"],
    },
    'Global Exposure': {
        'General': ["EWW", "EWZ", "ASHR", "EWG", "VEA"],
        'Technology': ["IXN", "KWEB", "QQQJ", "ARKK", "XITK"],
        'Energy': ["IXC", "IXG", "XES", "IPW", "KOL"],
    },
    # Need to determine best way to acquire commodities information
    'Commodities': {
        'Energy': ["USO", "UNG", "BNO", "DBO", "OIL"],
        'Metals': ["GLD", "SLV", "PALL", "PLTM", "IAU"],
        'Agriculture': ["DBA", "CORN", "WEAT", "SOYB", "COW"],
    },

    'Volatility Indices': {
        'General': ["VXX", "UVXY", "SVXY", "VIX"]
    }
}

nyse_sectors = {
    'sectors': {
            "Materials": ["DD", "LIN", "APD", "ECL", "SHW", "NEM", "FCX", "PPG", "CTVA", "IFF", "ALB", "AVY", "BMS",
                          "CE", "CF", "EMN", "FMC", "IP", "LYB", "MLM", "MOS", "NUE", "PKG", "RPM", "SEE", "VMC", "WRK",
                          "X", "GRA", "HUN", "ASH", "BCPC", "BHP", "BAS", "CC", "CMP", "CRS", "DOW", "EVA", "FUL",
                          "GGB", "GCP", "HXL", "KRO", "LTHM", "MT", "NGVT", "OLN", "RS", "SCCO", "TX", "UAN", "WPM",
                          "NTR", "VALE", "MP", "BTU", "TECK", "AA", "WLK", "WLKP", "FUL", "NEU", "OSB", "HUN", "MEOH",
                          "ACH", "CLF", "ATI", "MTRN", "KALU", "TROX", "AU", "PAAS", "GORO", "KGC", "SAND", "AG", "OR",
                          "SA", "SBSW", "HL", "NG", "BTG", "IAG", "CX", "EXP", "EAF", "RYAM", "LAC", "PLL", "LITM",
                          "LTHM", "SQM", "ALX", "BXP", "NGG"],

            "Industrials": ["MMM", "HON", "GE", "UPS", "BA", "CAT", "LMT", "RTX", "UNP", "DE", "EMR", "ETN", "ITW",
                            "GD", "NOC", "CSX", "FDX", "WM", "ROP", "JCI", "SWK", "TXT", "DOV", "IR", "PH", "PNR",
                            "PWR", "RSG", "SNA", "XYL", "ALLE", "AME", "AOS", "AXE", "B", "BKR", "BWXT", "CARR", "CMI",
                            "CW", "DHR", "DOV", "ETR", "FAST", "FLS", "FTV", "GWW", "HII", "IEX", "MTZ", "J", "NLSN",
                            "LECO", "EME", "FLS", "WSO", "TDG", "SWK", "OC", "NVR", "OC", "PII", "PWR", "PWR", "J",
                            "BLD", "TTEK", "URI", "TTEK", "TRMB", "J", "JBHT", "OC", "OSK", "HRI", "TTEK", "CSL",
                            "LECO", "WTS", "AGCO", "CNC", "GD", "NVT", "KBR", "CW", "BLD", "RBA", "MRCY", "CW", "REZI"],

            "Utilities": ["NEE", "DUK", "SO", "D", "AEP", "EXC", "SRE", "XEL", "ES", "PEG", "WEC", "ED", "EIX", "AWK",
                          "CMS", "DTE", "AEE", "ATO", "NI", "PNW", "PPL", "CNP", "FE", "EVRG", "AES", "NRG", "OGE",
                          "LNT", "IDA", "ALE", "AWR", "BKH", "CWT", "DTE", "EIX", "ETR", "MGEE", "NFG", "NJR", "OGS",
                          "ORA", "PNM", "POR", "SR", "SWX", "AVA", "BEP", "CWEN", "NEP", "PEGI", "PEG", "NRG", "UTL",
                          "ARTNA", "MGEE", "PNW", "LNT", "OGE", "PCG", "EIX", "WEC", "IDA", "CWT", "ALE", "EIX", "PNM",
                          "PNW", "LNT", "OGE", "ALE", "PCG", "NWE", "ORA", "PNM", "OGE", "ALE", "BKH", "OGS", "LNT",
                          "ALE", "PNW", "EIX", "LNT", "MGEE", "NFG", "OGS"],

            "Healthcare": ["JNJ", "UNH", "PFE", "ABBV", "MRK", "TMO", "ABT", "DHR", "LLY", "BMY", "MDT", "AMGN", "GILD",
                           "CVS", "CI", "HUM", "ISRG", "SYK", "BSX", "BDX", "ZTS", "VRTX", "REGN", "ILMN", "BIIB", "EW",
                           "IDXX", "ALGN", "ABC", "MCK", "A", "ALNY", "BAX", "BHC", "BIO", "BNTX", "CERN", "CRL", "DGX",
                           "DXCM", "HCA", "HOLX", "IQV", "LH", "MRNA", "MTD", "PODD", "RMD", "TFX", "STAA", "BIO",
                           "WAT", "TDOC", "CNC", "THC", "AKRO", "RETA", "VIR", "ISEE", "RLAY", "NVCR", "PBYI", "JAZZ",
                           "NKTR", "VEEV", "NBIX", "GBT", "AZN", "GSK", "SPRY", "OPRT", "BPMC", "FOLD", "VRNS", "GMAB",
                           "DNA", "KROS", "HCM", "EVGN", "ICLR", "PRAH", "LABP"],

            "Financials": ["JPM", "BAC", "WFC", "C", "GS", "MS", "AXP", "BLK", "SCHW", "SPGI", "CB", "MMC", "AON",
                           "MET", "PRU", "TRV", "AIG", "ALL", "PGR", "CME", "ICE", "NDAQ", "STT", "BK", "TROW", "AMP",
                           "LNC", "UNM", "L", "CINF", "AFL", "AIZ", "AJG", "AMP", "AON", "APO", "ARES", "BEN", "CBOE",
                           "CINF", "CMA", "DFS", "EVR", "FDS", "FRC", "GL", "HIG", "IVZ", "KKR", "LPLA", "MTB", "NAVI",
                           "NWBI", "OCFC", "OFG", "OPRT", "PB", "PACW", "PNC", "RF", "SBNY", "SIVB", "SNV", "STBA",
                           "TCBI", "UBSI", "UMPQ", "USB", "VLY", "WABC", "WBS", "WTFC", "ZION", "RY", "TD", "BNS", "CM",
                           "BMO", "MFC", "PFG", "RGA", "VOYA", "WETF", "XP", "OZK"],

            "Consumer Discretionary": ["AMZN", "TSLA", "HD", "NKE", "MCD", "SBUX", "LOW", "BKNG", "TJX", "GM", "F",
                                       "ROST", "EBAY", "YUM", "MAR", "HLT", "AZO", "ORLY", "DG", "DLTR", "ULTA", "LVS",
                                       "WYNN", "DHI", "LEN", "PHM", "NVR", "TOL", "WHR", "HAS", "AAP", "BBY", "BBWI",
                                       "BURL", "CCL", "CHWY", "CMG", "CZR", "DRI", "ETSY", "EXPE", "FND", "GPC", "GRMN",
                                       "HOG", "KMX", "KSS", "LEG", "LULU", "MTN", "NKE", "PLCE", "POOL", "RH", "RL",
                                       "ROST", "RUSHA", "RUTH", "SIG", "SIX", "SKX", "SPWH", "SWBI", "TCS", "THO",
                                       "TPR", "VFC", "WSM", "WING", "WRBY", "WW", "WYN", "YELP", "YUMC", "Z", "ZBRA",
                                       "ZYXI", "ACM"],

            "Consumer Staples": ["PG", "KO", "PEP", "WMT", "COST", "PM", "MO", "CL", "KMB", "MDLZ", "GIS", "KHC", "HSY",
                                 "SYY", "KR", "WBA", "ADM", "EL", "STZ", "CLX", "MKC", "CAG", "CPB", "CHD", "HRL", "K",
                                 "TSN", "LW", "BG", "TAP", "ACI", "ARMK", "BF.B", "BRFS", "BUD", "COTY", "DAR", "FDP",
                                 "FLO", "HAIN", "HRL", "INGR", "KDP", "KHC", "KMB", "KOF", "LW", "MKC", "FIZZ", "CPG",
                                 "MJN", "MNST", "NWL", "PRMW", "QSR", "RAD", "RAI", "STZ", "SWY", "THS", "TSN", "VGR",
                                 "WEN", "POST", "SAFM", "SJM", "UNFI", "VFF", "VLGEA", "WLK", "WEYS", "WILC", "CAG",
                                 "EL", "CLX", "POST"],

            "Information Technology": ["AAPL", "MSFT", "NVDA", "ADBE", "CSCO", "ORCL", "IBM", "INTC", "CRM", "TXN",
                                       "QCOM", "AVGO", "AMD", "NOW", "ADI", "MU", "LRCX", "AMAT", "KLAC", "SNPS",
                                       "CDNS", "ANSS", "FTNT", "PANW", "ZS", "OKTA", "DDOG", "MDB", "NET", "CRWD",
                                       "ACN", "AKAM", "ANET", "BR", "CDW", "CHKP", "CTSH", "DXC", "EPAM", "FFIV", "FIS",
                                       "FISV", "FLT", "GPN", "HPE", "HPQ", "NTAP", "ORCL", "OTEX", "PAYC", "RXT", "SAP",
                                       "SHOP", "SPLK", "SPT", "SQ", "STX", "SVMK", "TWLO", "TWTR", "VEEV", "WDAY",
                                       "WORK", "XM", "XLNX", "ZS", "ZM", "ZYXI", "ZUO", "AYX", "BCOR", "BLKB", "BOX",
                                       "CYBR", "DDOG", "DOCU", "DOX", "DXC", "DT"],

            "Communication Services": ["GOOGL", "META", "DIS", "NFLX", "VZ", "T", "TMUS", "CHTR", "CMCSA", "NWSA",
                                       "NWS", "FOXA", "FOX", "DISCA", "DISCK", "DISCB", "VIAC", "LUMN", "IPG", "OMC",
                                       "TTWO", "EA", "ATVI", "ROKU", "SPOT", "LYV", "FWONK", "SIRI", "IAC", "MTCH",
                                       "ATUS", "CABO", "CNSL", "DISH", "GOGO", "GSAT", "IDT", "IRDM", "LBRDA", "LBRDK",
                                       "LSXMA", "LSXMK", "NLSN", "NTES", "RNG", "BCE", "CHL", "CHU", "CNSL", "GOGO",
                                       "KT", "ORAN", "PHI", "RCI", "SJR", "SKM", "TEF", "TU", "VIV", "VOD", "YNDX",
                                       "ZTO", "ZM", "ZG", "ZI", "Z", "ZI", "ZG", "ZI", "ATUS", "CABO", "CNSL", "ATUS",
                                       "VOD", "VIV", "PHI"],

            "Real Estate": ["AMT", "PLD", "CCI", "EQIX", "PSA", "SPG", "O", "WELL", "DLR", "AVB", "EQR", "ESS", "MAA",
                            "UDR", "PEAK", "VTR", "ARE", "BXP", "SLG", "VNO", "HST", "WY", "DRE", "EXR", "CUBE", "INVH",
                            "SUI", "ELS", "IRM", "SBAC", "AIV", "AMH", "BRX", "BXP", "CPT", "CUZ", "EPR", "FRT", "HPP",
                            "KIM", "KRC", "LXP", "NNN", "OHI", "REG", "RHP", "RPT", "UDR", "ADC", "APLE", "DHC", "HR",
                            "IIPR", "IRT", "LADR", "LAMR", "LXP", "MAC", "MGRC", "NNN", "NSA", "PCH", "PSB", "PSTL",
                            "RFI", "RPT", "RWT", "SAFE", "SRC", "STOR", "STWD", "TCO", "UNIT", "VER", "VICI", "WRE",
                            "WPC"],
            "etf_symbols": [
                    "SPY",  # S&P 500®
                    "SCZ",  # MSCI EAFE Small Cap
                    "DIA",  # Dow Jones Industrial Average (DJIA)
                    "QQQ",  # NASDAQ
                    "EEM",  # MSCI Emerging Markets
                    "IWM",  # Russell 2000®
                    "LQD",  # Bloomberg US Credit
                    "EFA",  # MSCI EAFE®
                    "GSG",  # S&P GSCI® (Goldman Sachs Commodity Index)
                    "AGG"   # Bloomberg U.S. Aggregate Bond
                ]
        }
}
