import sqlite3
import pandas as pd

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def save_data(self, data, table_name='datos_procesados'):
        try:
            with sqlite3.connect(self.db_path) as conn:
                data.to_sql(table_name, conn, if_exists='replace', index=False)
        except Exception as e:
            raise e

    def load_data(self, table_name='datos_procesados'):
        try:
            with sqlite3.connect(self.db_path) as conn:
                return pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        except Exception as e:
            raise e
