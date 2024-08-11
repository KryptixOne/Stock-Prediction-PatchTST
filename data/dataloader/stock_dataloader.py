"""Dataloader for model"""

import os
import torch
from torch.utils.data import Dataset
import pandas as pd


class LazyStockDataset(Dataset):
    def __init__(self, directory, seq_length):
        self.seq_length = seq_length
        self.file_paths = []
        self.indices = []

        # Load all CSV files in the directory
        for file_name in os.listdir(directory):
            if file_name.endswith('.csv'):
                file_path = os.path.join(directory, file_name)
                df = pd.read_csv(file_path)
                # Create indices for sequences in this file
                for i in range(len(df) - seq_length + 1):
                    self.file_paths.append(file_path)
                    self.indices.append(i)

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, idx):
        file_path = self.file_paths[idx]
        start_idx = self.indices[idx]
        df = pd.read_csv(file_path, skiprows=range(1, start_idx), nrows=self.seq_length)

        # Extract features and label
        X = df.drop(columns=['label', 'symbol']).values
        y = df['label'].iloc[-1]

        return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.long)


"""# Example of initializing the dataset
directory = '/path/to/your/csv_directory'  # Replace with your directory path
seq_length = 30  # Example sequence length
dataset = LazyStockDataset(directory, seq_length)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
"""