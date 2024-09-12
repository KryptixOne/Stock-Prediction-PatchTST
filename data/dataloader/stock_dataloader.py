import os
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader


class StockForecastDataset(Dataset):
    def __init__(self, data_dir, window_size=90, transform=None):
        self.data_dir = data_dir
        self.window_size = window_size
        self.transform = transform
        self.sector_files = []
        self.data = []

        # Collect all CSV file paths in subdirectories
        for root, _, files in os.walk(data_dir):
            for file in files:
                if file.endswith(".csv"):
                    self.sector_files.append(os.path.join(root, file))

        # Load and preprocess data from each file
        for csv_path in self.sector_files:
            df = pd.read_csv(csv_path)
            df = self.preprocess_data(df)
            self.data.extend(df)

    def preprocess_data(self, df):
        # Ensure the dataframe is sorted by date
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp').reset_index(drop=True)

        # Extract relevant features (open, close, volume) and labels
        features = df[['1. open', '4. close', '6. volume']].values
        labels = df[['Forecast 1 Week', 'Forecast 2 Week', 'Forecast 3 Week', 'Forecast 4 Week']].values

        # Create sliding windows of 90 days
        windowed_data = []
        for i in range(len(df) - self.window_size):
            window = features[i:i + self.window_size]
            target_labels = labels[i + self.window_size - 1]  # Labels for the most recent day of the window
            windowed_data.append((window, target_labels))

        return windowed_data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        features, labels = self.data[idx]
        features = torch.tensor(features, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.long)  # Labels are categorical

        if self.transform:
            features = self.transform(features)

        return features, labels


# Example usage of DataLoader
data_dir = '/path/to/your/dataset'
window_size = 90
batch_size = 32

# Instantiate dataset
dataset = StockForecastDataset(data_dir=data_dir, window_size=window_size)

# Create DataLoader
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Example iteration through DataLoader
for batch_features, batch_labels in dataloader:
    print("Batch features shape:", batch_features.shape)  # Should be [batch_size, 90, 3]
    print("Batch labels shape:", batch_labels.shape)  # Should be [batch_size, 4]
    # These would be fed into your model
