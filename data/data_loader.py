import pandas as pd

class DataLoader:
    def __init__(self):
        self.df = None

    def load_csv(self, filepath):
        self.df = pd.read_csv(filepath)
        return self.df
