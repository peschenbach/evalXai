# %% Imports
import matplotlib.pyplot as plt
from utils import DataLoader

# %% Load data
data_loader = DataLoader()
data_loader.load_data()
data = data_loader.data

print(data.shape)