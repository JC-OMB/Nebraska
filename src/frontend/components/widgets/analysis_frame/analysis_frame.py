from tkinter import Frame
from tkinter.ttk import Combobox

from api.api import API
from frontend.components.widgets.analysis_frame.dataframe_widget import DataFrameWidget


class AnalysisFrame(Frame):
    _instance = None
    label = 'Analysis'

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(AnalysisFrame, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Create widgets
            self.setup()

    def setup(self):
        # Create widgets
        self.add_widgets()
        # Pack
        self.data_selector.pack(fill='x')

    def add_widgets(self):
        self.data_selector = Combobox(self, state="readonly")
        self.data_selector.bind("<<ComboboxSelected>>", self.select)
        self.data_selector.set("Select Schema")
        self.table = DataFrameWidget(self)

    def select(self, event=None):
        selected_name = self.data_selector.get()
        self.table.load(selected_name)

    def update_combobox(self):
        values = API.data.get_names()
        self.data_selector['values'] = values
