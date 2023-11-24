from pandas import read_csv
from pandas.errors import EmptyDataError, ParserError

from api.controllers.file_controllers.csv_controller import CSVController
from api.controllers.schema_controllers.schema_controller import SchemaController


class DatasetController:
    datasets = {}

    @classmethod
    def add(cls, dataset):
        name = dataset["path"].name
        cls.datasets[name] = dataset

    @classmethod
    def get(cls, name):
        return cls.datasets[name]

    @classmethod
    def get_data(cls, name):
        return cls.get(name)["df"]

    @classmethod
    def get_schema(cls, name):
        return cls.get(name)["schema"]

    @classmethod
    def get_names(cls):
        return list(cls.datasets.keys())

    @classmethod
    def load_one(cls, path):
        name = path.name
        try:
            df = read_csv(path)
            if df.empty:
                raise ValueError("CSV file is empty")
            schema = SchemaController.get(df)
            dataset = {"path": path, "df": df, "schema": schema}
            cls.add(dataset)
        except (FileNotFoundError, ParserError, EmptyDataError) as e:
            # Handle specific file reading and parsing errors
            print(f"Error reading file {name}: {e}")
            return None
        except ValueError as e:
            # Handle validation errors
            print(f"Validation error for file {name}: {e}")
            return None

    @classmethod
    def load_all(cls):
        for path in CSVController.selected:
            cls.load_one(path)
