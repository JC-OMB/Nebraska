from tkinter import Frame, Button, Label


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
        # Checkbox
        row_frame = Frame(self)

        label = Label(row_frame, text=self.path.name)
        label.pack(side='left')

        remove_btn = Button(row_frame, text="Remove", fg="red", command=lambda p=self.path: self.remove_row(p))
        remove_btn.pack(side='right')

        row_frame.pack(anchor='n', fill='x')

    def render(self):
        self.pack(anchor='n', fill='x')
