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

        # Collect all CSV file paths in subdirectories, except "Economic_Data"
        for root, dirs, files in os.walk(data_dir):
            if 'Economic_Data' in dirs:
                dirs.remove('Economic_Data')  # Exclude the 'Economic_Data' directory
            for file in files:
                if file.endswith(".csv"):
                    self.sector_files.append(os.path.join(root, file))

        # Store the total length (number of sliding windows across all files)
        self.total_windows = self._calculate_total_windows()

    def _calculate_total_windows(self):
        total_windows = 0
        for csv_path in self.sector_files:
            df = pd.read_csv(csv_path)
            total_windows += max(0, len(df) - self.window_size)
        return total_windows

    def _get_data_from_file(self, csv_path, start_idx):
        # Read the specific CSV file and return the data corresponding to the window
        df = pd.read_csv(csv_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp').reset_index(drop=True)

        # Extract relevant features (open, close, volume) and labels
        features = df[['1. open', '2. high', '3. low', '4. close', '5. adjusted close', '6. volume']].values
        labels = df[['Forecast 1 Week', 'Forecast 2 Week', 'Forecast 3 Week', 'Forecast 4 Week']].values

        # Return the sliding window and the corresponding labels
        window_features = features[start_idx:start_idx + self.window_size]
        window_labels = labels[start_idx + self.window_size - 1]  # Labels for the most recent day of the window

        return window_features, window_labels

    def __len__(self):
        return self.total_windows

    def __getitem__(self, idx):
        # Locate the corresponding CSV file and sliding window based on idx
        window_count = 0
        for csv_path in self.sector_files:
            df = pd.read_csv(csv_path)
            num_windows = max(0, len(df) - self.window_size)
            if window_count + num_windows > idx:
                # This file contains the required window
                file_idx = idx - window_count
                features, labels = self._get_data_from_file(csv_path, file_idx)
                break
            window_count += num_windows

        # Convert to torch tensors
        features = torch.tensor(features, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.long)  # Labels are categorical

        if self.transform:
            features = self.transform(features)

        return features, labels
