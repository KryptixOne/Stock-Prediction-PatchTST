import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Load data
df = pd.read_csv('Data/SPY_Daily_Data.csv')


# Assume 'timestamp' is the date column, and other columns are present as required
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Select relevant features
features = df[['open', 'high', 'low', 'close', 'volume']]



# Initialize scalers for each feature
scalers = {}
multiplier = 3
for feature in features.columns:
    print(df[feature].max())
    new_max =
    scalers[feature] = MinMaxScaler(feature_range=(0, 1))

# Fit and transform each feature independently
scaled_features = pd.DataFrame(index=features.index)
for feature in features.columns:
    scaled_features[feature] = scalers[feature].fit_transform(features[[feature]])
