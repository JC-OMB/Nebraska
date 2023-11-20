class Database:
    def __init__(self):
        # Paths
        self.csv_sources = set()
        self.csv_selected = set()

    def add_csv(self, path):
        self.csv_sources.add(path)

    def add_csvs(self, paths):
        for path in paths:
            self.add_csv(path)

    def remove_csv(self, path):
        self.csv_sources.discard(path)
        self.csv_selected.discard(path)

    def select_csv(self, path, value):
        if value:
            self.csv_selected.add(path)
        else:
            self.csv_selected.discard(path)
