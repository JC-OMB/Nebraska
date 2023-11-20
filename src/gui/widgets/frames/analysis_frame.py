from tkinter import Label, Frame
from tkinter.ttk import Combobox


class AnalysisFrame(Frame):
    label = 'Analysis'

    def __init__(self, master):
        super().__init__(master)
        self.db = master.db
        self.data_adapter = master.data_adapter

        self.add_widgets()
        self.render()

    def add_widgets(self):
        self.csv_selector = Combobox(self, state="readonly")
        self.csv_selector.bind("<<ComboboxSelected>>", self.update_selected_path_label)
        self.csv_selector.pack(fill='x')

        self.selected_path_label = Label(self, text="")
        self.selected_path_label.pack()

    def update_combobox(self):
        self.csv_selector['values'] = [path for path in self.data_adapter.dataframes.keys()]

    def update_selected_path_label(self, event=None):
        selected_path_name = self.csv_selector.get()
        selected_path = self.data_adapter.dataframes[selected_path_name]["path"]
        self.selected_path_label.config(text=selected_path)

    def render(self):
        # Additional rendering logic (if any)
        pass
