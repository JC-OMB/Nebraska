from tkinter import Tk

from frontend.components.notebooks import MainNotebook


class Frontend(Tk):
    def __init__(self, api):
        # Initialize the main window
        super().__init__()
        # Set up api
        self.api = api

        # Set up the main window
        self.title("Data Analysis Application")
        self.geometry("800x600")
        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        MainNotebook(self)

    def render(self):
        # Start the main loop
        self.mainloop()
