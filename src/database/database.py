from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models import Dataset, Metric, Sensor, Site


class Database:
    def __init__(self):
        self.models = [Site, Sensor, Metric, Dataset]
        self.url = 'sqlite:///src/database/data/database.db'
        self.engine = create_engine(self.url, echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        for model in self.models:
            model.metadata.create_all(self.engine)

    def run(self):
        self.create_tables()
