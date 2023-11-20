from pathlib import Path
from tkinter import messagebox


class Database:
    def __init__(self):
        # Paths
        self.csv_paths = set()
        self.selected_csv_paths = set()
        # Data

    def add_csv(self, path):
        self.csv_paths.add(path)

    def add_csvs(self, paths):
        for path in paths:
            self.add_csv(path)

    def load_csvs(self):
        if self.selected_csv_paths:
            messagebox.showinfo("Load CSV", "Files loaded successfully")
        else:
            messagebox.showerror(title="Error", message="Error: No files selected")

    def remove_csv(self, path):
        self.csv_paths.discard(path)
        self.selected_csv_paths.discard(path)

    def select_csv(self, path, value):
        if value:
            self.selected_csv_paths.add(path)
        else:
            self.selected_csv_paths.discard(path)