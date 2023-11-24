class SchemaController:
    sources = set()

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

    @classmethod
    def get(cls, dataset):
        pass
