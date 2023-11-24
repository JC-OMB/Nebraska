from database.database import Database
from frontend.frontend import Frontend


class App:
    db = Database
    frontend = Frontend()

    @classmethod
    def run(cls):
        cls.db.run()
        cls.frontend.render()
