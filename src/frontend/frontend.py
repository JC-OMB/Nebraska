from tkinter import Tk

from frontend.components.notebooks.main_notebook import MainNotebook


class Frontend(Tk):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Frontend, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self):
        if not self.initialized:
            # Initialize
            super().__init__()
            self.initialized = True
            # Setup
            self.setup()

    def setup(self):
        # Set up the main window
        self.title("Data ANALysis Tool")
        self.geometry("800x600")
        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        MainNotebook(self)

    def render(self):
        # Start the main loop
        self.mainloop()
