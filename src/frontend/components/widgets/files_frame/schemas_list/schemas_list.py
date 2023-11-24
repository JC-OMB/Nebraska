from pathlib import Path
from tkinter import Frame, filedialog, Button

from api.api import API
from frontend.components.widgets.files_frame.schemas_list.schema_row import SchemaRow


class SchemaList(Frame):
    def __init__(self, master):
        # Initialize
        super().__init__(master)
        self.initialized = True
        # Create widgets
        self.add_widgets()
        # Render
        self.render()

    def add_row(self, path):
        if path not in API.schema.sources:
            API.schema.load(path)
            SchemaRow(self, path)

    def add_rows(self):
        # Get CSV paths
        paths = filedialog.askopenfilenames(title="Open Schema files", filetypes=[("CSV files", "*.csv")])
        # Convert paths to Path objects
        paths = [Path(path) for path in paths]
        # Add CSV paths to database
        for path in paths:
            self.add_row(path)

    def add_widgets(self):
        # Add Schema Button
        self.add_schema_button = Button(self, text="Add Schema(s)", command=self.add_rows)

    def render(self):
        self.add_schema_button.pack(anchor='center')
        self.pack(anchor='n', fill='x')

    def reload(self):
        if len(API.schema.sources) == 0:
            self.config(height=1)
