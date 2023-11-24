class CSVController:
    sources = set()
    selected = set()

    @classmethod
    def add(cls, path):
        cls.sources.add(path)

    @classmethod
    def add_all(cls, paths):
        for path in paths:
            cls.add(path)

    @classmethod
    def remove(cls, path):
        cls.sources.discard(path)
        cls.selected.discard(path)

    @classmethod
    def select_one(cls, path, value):
        if value:
            cls.selected.add(path)
        else:
            cls.selected.discard(path)
