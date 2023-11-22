import pandas as pd
import json

class DataExporter:
    def __init__(self, data):
        self.data = data

    def export_csv(self, filepath):
        try:
            self.data.to_csv(filepath, index=False)
        except Exception as e:
            raise e

    def export_json(self, filepath, metadata):
        try:
            with open(filepath, 'w') as f:
                json.dump(metadata, f)
        except Exception as e:
            raise e
