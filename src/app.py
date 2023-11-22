from api import API
from database import Database
from frontend import Frontend


class App:
    def __init__(self):
        # Database
        self.db = Database()
        # API
        self.api = API()
        # Frontend
        self.frontend = Frontend(self.api)

    def run(self):
        self.db.run()
        self.frontend.render()
