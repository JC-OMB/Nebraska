from tkinter import Frame


class VisualizationFrame(Frame):
    _instance = None
    label = "Visualization"

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(VisualizationFrame, cls).__new__(cls)
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
        pass

    def render(self):
        pass
