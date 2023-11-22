from tkinter import Frame


class ExportFrame(Frame):
    label = "Export"

    def __init__(self, master):
        super().__init__(master)

        self.add_widgets()

        self.render()

    def add_widgets(self):
        pass

    def render(self):
        pass
