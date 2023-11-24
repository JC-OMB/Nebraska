from tkinter.ttk import Notebook

from frontend.components.widgets.widget_factory import WidgetFactory


class MainNotebook(Notebook):
    _instance = None

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(MainNotebook, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Add widgets
            self.add_widgets()
            # render
            self.render()

    def add_widgets(self):
        widgets = WidgetFactory.get(MainNotebook)
        for widget in widgets:
            self.add(widget(self), text=widget.label)

    def render(self):
        # Pack
        self.pack(expand=True, fill='both')
