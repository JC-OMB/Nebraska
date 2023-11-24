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
    def get_names(cls):
        return [path.stem for path in cls.sources]

    @classmethod
    def get_all(cls):
        return cls.sources

    @classmethod
    def remove(cls, path):
        cls.sources.discard(path)

    @classmethod
    def get(cls, dataset):
        pass
