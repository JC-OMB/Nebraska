from pandas import read_csv, merge

from api.controllers.file_controllers.csv_controller import CSVController


class DatasetController:
    datasets = {}

    @classmethod
    def add(cls, path):
        cls.datasets[path] = read_csv(path)

    @classmethod
    def get(cls, path):
        return cls.datasets[path]

    @classmethod
    def load(cls):
        for selected_path in CSVController.selected:
            cls.add(selected_path)

    @classmethod
    def merge(cls):
        dataset = None
        for path in cls.datasets.keys():
            df = cls.get(path)
            if dataset is None:
                dataset = df
            else:
                dataset = merge(dataset, df, on='startDateTime')
        cls.datasets["universal"] = dataset
