import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from pandas import read_csv


class DataAdapter:
    def __init__(self, db):
        self.db = db
        self.dataframes = {}

    def load_csv(self, path):
        df = read_csv(path)
        return path, df

    def load_csvs(self):
        max_workers = os.cpu_count()
        with ThreadPoolExecutor(max_workers) as executor:
            futures = {executor.submit(self.load_csv, path): path for path in self.db.csv_selected}
            for future in as_completed(futures):
                path, df = future.result()
                self.dataframes[path.name] = dict(path=path, df=df)
