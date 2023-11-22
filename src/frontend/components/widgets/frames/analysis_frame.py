from tkinter import Frame
from tkinter.ttk import Combobox

from frontend.components.widgets.trees import DataFrameWidget


class AnalysisFrame(Frame):
    label = 'Analysis'

    def __init__(self, master):
        super().__init__(master)
        self.api = master.api

        self.add_widgets()
        self.render()

    def add_widgets(self):
        self.data_selector = Combobox(self, state="readonly")
        self.data_selector.bind("<<ComboboxSelected>>", self.select)
        self.table = DataFrameWidget(self)

    def select(self, event=None):
        selected_name = self.data_selector.get()
        self.table.load(selected_name)

    def update_combobox(self):
        values = self.api.data.get_keys()
        self.data_selector['values'] = values

    def render(self):
        self.data_selector.pack(fill='x')
        self.table.render()
