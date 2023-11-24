from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.models.dataset import Dataset
from api.models.metric import Metric
from api.models.sensor import Sensor
from api.models.site import Site


class Database:
    engine = None
    models = None
    session = None
    url = None

    @classmethod
    def setup(cls):
        # Set up the database
        cls.models = [Dataset, Metric, Sensor, Site]
        cls.url = 'sqlite:///src/database/data/database.db'
        cls.engine = create_engine(cls.url)
        cls.session = sessionmaker(bind=cls.engine)
        # Create tables
        cls.create_tables()

    @classmethod
    def create_tables(cls):
        for model in cls.models:
            model.metadata.create_all(cls.engine)

    @classmethod
    def run(cls):
        # Setup
        cls.setup()
