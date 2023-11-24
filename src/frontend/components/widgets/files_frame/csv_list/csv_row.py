from tkinter import Frame, BooleanVar, Checkbutton, Button

from api.api import API


class CSVRow(Frame):
    def __init__(self, master, path):
        super().__init__(master)
        # Setup
        self.path = path
        API.csv.add(self.path)
        # Add widgets
        self.add_widgets()
        # Render
        self.render()

    def add_widgets(self):
        text = self.path.name
        var = BooleanVar(value=self.path in API.csv.selected)
        command = lambda: self.select_row(self.path, var)
        self.checkbox = Checkbutton(self, text=text, var=var, command=command)
        # Remove Button
        self.remove_btn = Button(self, text="Remove", fg="red", command=self.destroy)

    def render(self):
        self.checkbox.pack(side='left')
        self.remove_btn.pack(side='right')
        self.pack(anchor='n', fill='x')

    def destroy(self):
        API.csv.remove(self.path)
        super().destroy()

    def select_row(self, path, var):
        is_selected = var.get()
        API.csv.select_one(path, is_selected)
        self.master.master.handle_load_button()
