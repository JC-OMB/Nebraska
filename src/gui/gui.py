from tkinter import Tk

from gui.notebooks import MainNotebook


class GUI(Tk):
    def __init__(self, db):
        # Initialize the main window
        super().__init__()
        # Set up data
        self.db = db

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
