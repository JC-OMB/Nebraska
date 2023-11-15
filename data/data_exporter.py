class DataExporter:
    def __init__(self, data):
        self.data = data

    def export_csv(self, filepath):
        self.data.to_csv(filepath, index=False)

    def export_json(self, filepath, metadata):
        # Implementation for exporting metadata as JSON
        pass
