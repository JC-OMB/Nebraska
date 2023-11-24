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
        df1 = None
        for path in cls.datasets.keys():
            df2 = cls.get(path)
            if df1 is None:
                df1 = df2
            else:
                df1 = merge(df1, df2, on='startDateTime')
        cls.datasets["universal"] = df1

    # TODO: Implement self.export
