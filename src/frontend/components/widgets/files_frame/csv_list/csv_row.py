from tkinter import Frame, BooleanVar, Checkbutton, Button
from tkinter.ttk import Combobox

from api.api import API


class CSVRow(Frame):
    def __init__(self, master, path):
        super().__init__(master)
        # Setup
        self.path = path
        # Add widgets
        self.add_widgets()
        # Render
        self.render()

    def add_widgets(self):
        # Checkbox
        label = self.path.stem
        selection = BooleanVar(value=self.path in API.csv.selected)
        command = lambda: self.select_row(self.path, selection)
        checkbox = Checkbutton(self, text=label, var=selection, command=command)
        checkbox.pack(side='left')
        # Schema Dropdown
        schema_options = [schema.name for schema in API.schema.sources]
        schema_dropdown = Combobox(self, values=schema_options, state="readonly")
        schema_dropdown.set("Select Schema")

        remove_btn = Button(self, text="Remove", fg="red", command=lambda p=self.path: self.remove_row(p))

        remove_btn.pack(side='right')
        schema_dropdown.pack(side='right')

    def render(self):
        self.pack(anchor='n', fill='x')
        self.master.master.render_load_button()

    def remove_row(self, path):
        API.csv.remove(path)
        self.destroy()
        self.master.render()

    def select_row(self, path, selection):
        is_selected = selection.get()
        API.csv.select_one(path, is_selected)
        self.render()
