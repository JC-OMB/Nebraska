from tkinter import Frame


class HomeFrame(Frame):
    _instance = None
    label = 'Home'

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(HomeFrame, cls).__new__(cls)
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
        # TODO - Add widgets for home frame
        # Título, fotos, enlaces a la documentación, etc.
        pass

    def render(self):
        pass
