from pathlib import Path
from tkinter import Frame, filedialog, Button

from api.api import API
from frontend.components.widgets.files_frame.csv_list.csv_row import CSVRow


class CSV_List(Frame):
    def __init__(self, master):
        # Initialize
        super().__init__(master)
        self.initialized = True
        # Create widgets
        self.add_widgets()
        # Render
        self.render()

    def add_widgets(self):
        self.add_button = Button(self, text="Add Dataset(s)", command=self.add_rows)

    def render(self):
        self.add_button.pack(anchor='n')
        self.pack(anchor='center', fill='x')

    def add_row(self, path):
        if path not in API.csv.sources:
            CSVRow(self, path)

    def add_rows(self):
        # Get CSV paths
        paths = filedialog.askopenfilenames(title="Open CSV files", filetypes=[("CSV files", "*.csv")])
        # Convert paths to Path objects
        paths = [Path(path) for path in paths]
        # Add CSV paths to database
        for path in paths:
            self.add_row(path)
