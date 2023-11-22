class CSVController:
    def __init__(self):
        # Paths
        self.sources = set()
        self.selected = set()

    def add(self, path):
        self.sources.add(path)

    def add_all(self, paths):
        for path in paths:
            self.add(path)

    def remove(self, path):
        self.sources.discard(path)
        self.selected.discard(path)

    def select_one(self, path, value):
        if value:
            self.selected.add(path)
        else:
            self.selected.discard(path)

    def select_some(self, paths, value):
        for path in paths:
            self.select_one(path, value)
