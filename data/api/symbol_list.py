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

sector_list = ['General', 'Technology', 'Consumer Discretionary', 'Energy',
               'Healthcare', 'Industrials', 'Consumer Staples',
               'Communication Services', 'Utilities', 'Metals', 'Agriculture']

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
    'Commodities': {
        'Energy': ["USO", "UNG", "BNO", "DBO", "OIL"],
        'Metals': ["GLD", "SLV", "PALL", "PLTM", "IAU"],
        'Agriculture': ["DBA", "CORN", "WEAT", "SOYB", "COW"],
    },

    'Volatility Indices': {
        'General': ["VXX", "UVXY", "SVXY", "VIX"]
    }
}
