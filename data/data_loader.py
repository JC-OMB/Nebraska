import pandas as pd

class DataLoader:
    def __init__(self):
        self.df = None

    def load_csv(self, filepath):
        self.df = pd.read_csv(filepath)
        return self.df
    
    #Limpiara el csv para que se pueda seleccionar las columnas
    def clean_column_names(self):
        self.df.columns = [col.strip().rstrip(',') for col in self.df.columns]


