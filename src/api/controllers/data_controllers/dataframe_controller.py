from pandas import read_csv
from pandas.errors import ParserError, EmptyDataError


class DataFrameController:
    def __init__(self):
        self.dataframes = {}

    def add(self, name, data):
        self.dataframes[name] = data

    def get(self, name):
        return self.dataframes[name]['util']

    def get_full(self, name):
        return self.dataframes[name]

    def get_keys(self):
        return list(self.dataframes.keys())

    def from_csv(self, path):
        try:
            df = read_csv(path)
            if df.empty:
                raise ValueError("CSV file is empty")
            return df
        except (FileNotFoundError, ParserError, EmptyDataError) as e:
            # Handle specific file reading and parsing errors
            print(f"Error reading file {path}: {e}")
            return None
        except ValueError as e:
            # Handle validation errors
            print(f"Validation error for file {path}: {e}")
            return None
