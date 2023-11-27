import pandas as pd

class DataLoader():
    def __init__(self):
        self.data = None

    def load_data(self, path="data/data.csv"):
        self.data = pd.read_csv(path)