from tkinter import Frame


class ExportFrame(Frame):
    _instance = None
    label = "Export"

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(ExportFrame, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Add widgets
            self.add_widgets()
            # Initial Render
            self.render()

    def add_widgets(self):
        # TODO - Add widgets for exporting data
        # ...
        # API.data.export()
        pass

    def render(self):
        pass
