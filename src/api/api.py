from api.controllers.dataset_controllers.dataset_controller import DatasetController
from api.controllers.file_controllers.csv_controller import CSVController
from api.controllers.schema_controllers.schema_controller import SchemaController


class API:
    csv = CSVController
    data = DatasetController
    schema = SchemaController
