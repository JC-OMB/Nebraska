from api.controllers import CSVController, DataController


class API:
    def __init__(self):
        self.csv = CSVController()
        self.data = DataController()
