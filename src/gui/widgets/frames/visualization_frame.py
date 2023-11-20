from tkinter import Frame


class VisualizationFrame(Frame):
    label = "Visualization"

    def __init__(self, master):
        super().__init__(master)

        self.create_widgets()

    def create_widgets(self):
        pass
