from tkinter import Frame,Label,ttk,Text


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
        text_label = ttk.Label(self, text="Nebraska Project", font=("Helvetica", 25, "bold"))
        text_label.pack()
        description_text = Text(self, wrap="word", height=5, width=40)
        description_text.insert("1.0", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                                      "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                                      "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
                                      "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
                                      "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
                                      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
                                      "deserunt mollit anim id est laborum.")
        description_text.config(state="disabled")
        description_text.pack(pady=10)
        pass

    def render(self):
        pass
