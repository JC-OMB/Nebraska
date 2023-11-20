from tkinter.ttk import Notebook

from gui.widgets.widget_factory import WidgetFactory


class MainNotebook(Notebook):
    label = "Main Notebook"

    def __init__(self, master):
        super().__init__(master)
        # Set up data
        self.db = master.db
        self.data_adapter = master.data_adapter
        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        widgets = WidgetFactory.get_widgets(self)
        for widget in widgets:
            self.add(widget(self), text=widget.label)
        self.pack(expand=True, fill='both')
