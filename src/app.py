from data.database import Database
from gui import GUI


class App:
    def __init__(self):
        # Backend
        self.db = Database()
        # Frontend
        self.gui = GUI(self.db)

    def run(self):
        self.gui.render()
