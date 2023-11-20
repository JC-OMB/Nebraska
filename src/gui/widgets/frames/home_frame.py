from tkinter import Frame


class HomeFrame(Frame):
    label = 'Home'

    def __init__(self, master):
        super().__init__(master)

        self.add_widgets()

    def add_widgets(self):
        pass
