import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=50, output_size=1):
        super(LSTMModel, self).__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size)
        self.linear = nn.Linear(hidden_layer_size, output_size)
        self.hidden_cell = (torch.zeros(1, 1, self.hidden_layer_size),
                            torch.zeros(1, 1, self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq), 1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)


# Load data
df = pd.read_csv('Data/SPY_Daily_Data.csv')

# Assume 'timestamp' is the date column, and other columns are present as required
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.set_index('timestamp', inplace=True)

# Select relevant features
features = df[['open', 'high', 'low', 'close', 'volume']]

assert not df.isnull().values.any(), 'NaN Values present'

# Assuming the CSV has a column 'Close' which we want to predict
data = df['close'].values
data = data.reshape(-1, 1)

# Normalize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Split the data into training, validation, and test sets (60%, 20%, 20%)
train_size = int(len(scaled_data) * 0.6)
val_size = int(len(scaled_data) * 0.2)
test_size = len(scaled_data) - train_size - val_size

train, val, test = scaled_data[:train_size, :], scaled_data[train_size:train_size+val_size, :], scaled_data[train_size+val_size:, :]


look_back = 10
X_train, Y_train = create_dataset(train, look_back)
X_val, Y_val = create_dataset(val, look_back)
X_test, Y_test = create_dataset(test, look_back)

# Convert data to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1)
Y_train = torch.tensor(Y_train, dtype=torch.float32)
X_val = torch.tensor(X_val, dtype=torch.float32).unsqueeze(1)
Y_val = torch.tensor(Y_val, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(1)
Y_test = torch.tensor(Y_test, dtype=torch.float32)




model = LSTMModel()
loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)



epochs = 100

for i in range(epochs):
    model.train()
    for seq, labels in train_loader:
        optimizer.zero_grad()
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                             torch.zeros(1, 1, model.hidden_layer_size))

        y_pred = model(seq)

        single_loss = loss_function(y_pred, labels)
        single_loss.backward()
        optimizer.step()

    model.eval()
    val_loss = 0
    with torch.no_grad():
        for seq, labels in val_loader:
            model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                                 torch.zeros(1, 1, model.hidden_layer_size))
            y_pred = model(seq)
            val_loss += loss_function(y_pred, labels).item()

    if i % 25 == 1:
        print(f'epoch: {i:3} train loss: {single_loss.item():10.8f} val loss: {val_loss/len(val_loader):10.8f}')

# Make predictions
model.eval()
train_predict = []
test_predict = []

with torch.no_grad():
    for seq, labels in train_loader:
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                             torch.zeros(1, 1, model.hidden_layer_size))
        train_predict.append(model(seq).item())

    for seq, labels in test_loader:
        model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                             torch.zeros(1, 1, model.hidden_layer_size))
        test_predict.append(model(seq).item())

# Invert predictions
train_predict = scaler.inverse_transform(np.array(train_predict).reshape(-1, 1))
Y_train = scaler.inverse_transform(Y_train.numpy().reshape(-1, 1))
test_predict = scaler.inverse_transform(np.array(test_predict).reshape(-1, 1))
Y_test = scaler.inverse_transform(Y_test.numpy().reshape(-1, 1))

# Plot baseline and predictions
plt.plot(scaler.inverse_transform(scaled_data))
plt.plot(np.append(np.empty((look_back,1))*np.nan, train_predict))
plt.plot(np.append(np.empty((len(train_predict)+(look_back*2)+1,1))*np.nan, test_predict))
plt.show()
