from api.controllers.data_controllers.dataframe_controller import DataFrameController


class DataController(DataFrameController):
    def __init__(self):
        super().__init__()

    def load_csv(self, csv, path):
        name = path.name
        data = {"path": path, "util": self.from_csv(path)}
        self.add(name, data)

    def load_csvs(self, csv):
        for path in csv.selected:
            self.load_csv(csv, path)
