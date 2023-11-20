from data import DataAdapter, Database
from gui import GUI


class App:
    def __init__(self):
        # Backend
        self.db = Database()
        self.data_adapter = DataAdapter(self.db)
        self.db.data_adapter = self.data_adapter
        # Frontend
        self.gui = GUI(self.db, self.data_adapter)

    def run(self):
        self.gui.render()
