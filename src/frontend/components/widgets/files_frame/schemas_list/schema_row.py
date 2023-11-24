from tkinter import Frame, Button, Label

from api.api import API


class SchemaRow(Frame):
    def __init__(self, master, path):
        super().__init__(master)
        # Setup
        self.path = path
        # Add widgets
        self.add_widgets()
        # Render
        self.render()

    def add_widgets(self):
        self.label = Label(self, text=self.path.name)
        # Remove button
        self.remove_btn = Button(self, text="Remove", fg="red", command=self.destroy)

    def destroy(self):
        API.schema.remove(self.path)
        super().destroy()

    def render(self):
        self.label.pack(side='left')
        self.remove_btn.pack(side='right')
        self.pack(anchor='n', fill='x')
