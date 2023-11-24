from pathlib import Path
from tkinter import Frame, filedialog

from api.api import API
from frontend.components.widgets.files_frame.csv_list.csv_row import CSVRow


class CSV_List(Frame):
    def __init__(self, master):
        # Initialize
        super().__init__(master)
        self.initialized = True

    def add_row(self, path):
        API.csv.add(path)
        CSVRow(self, path)

    def add_rows(self):
        # Get CSV paths
        paths = filedialog.askopenfilenames(title="Open CSV files", filetypes=[("CSV files", "*.csv")])
        # Convert paths to Path objects
        paths = [Path(path) for path in paths]
        # Add CSV paths to database
        for path in paths:
            self.add_row(path)
        # Render rows
        self.render()

    def render(self):
        # Self
        self.pack_forget()
        if API.csv.sources:
            self.pack(anchor='n', fill='x')
        # Master
        self.master.render_add_button()
        self.master.render_load_button()
