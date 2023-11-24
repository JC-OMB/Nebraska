from pathlib import Path
from tkinter import Frame, Button, filedialog

from api.api import API
from frontend.components.widgets.files_frame.schemas_list.schema_row import SchemaRow


class SchemasList(Frame):
    def __init__(self, master):
        # Initialize
        super().__init__(master)
        self.initialized = True
        # Create widgets
        self.add_widgets()

    def add_widgets(self):
        self.list = Frame(self)
        self.add_button = Button(self, text="Add Schema(s)", command=self.add_rows)

    def add_row(self, path):
        SchemaRow(self.list, path)

    def add_rows(self):
        # Get CSV paths
        paths = filedialog.askopenfilenames(title="Open Schema files", filetypes=[("CSV files", "*.csv")])
        # Convert paths to Path objects
        paths = [Path(path) for path in paths]
        # Add CSV paths to database
        API.schema.add_all(paths)
        # Render rows
        self.render_rows()

    def remove_row(self, path):
        API.schema.remove(path)
        self.render_rows()

    def render(self):
        self.render_list()
        self.render_add_button()
        self.pack(anchor='n', fill='x')
        self.master.render_load_button()

    def render_add_button(self):
        self.add_button.pack_forget()
        if len(API.schema.sources) < 4:
            self.add_button.pack(anchor='center')

    def render_list(self):
        self.list.pack_forget()
        if API.schema.sources:
            self.list.pack(anchor='n', fill='x')

    def render_rows(self):
        # Destroy Rows
        [row.destroy() for row in self.list.winfo_children()]
        # Render Rows
        for path in API.schema.sources:
            self.add_row(path)
        # Toggle Buttons
        self.render()
