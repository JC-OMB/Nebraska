from api.controllers.dataset_controllers.dataset_controller import DatasetController
from api.controllers.file_controllers.csv_controller import CSVController


class API:
    csv = CSVController
    data = DatasetController
