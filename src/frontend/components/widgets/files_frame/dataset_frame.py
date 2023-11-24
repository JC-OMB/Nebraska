from tkinter import Frame, Button, messagebox

from api.api import API
from api.controllers.dataset_controllers.dataset_controller import DatasetController
from frontend.components.widgets.analysis_frame.analysis_frame import AnalysisFrame
from frontend.components.widgets.files_frame.csv_list.csv_list import CSV_List


class DatasetFrame(Frame):
    _instance = None
    label = "Datasets"

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(DatasetFrame, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Create widgets
            self.add_widgets()
            # Render
            self.render()

    def add_widgets(self):
        # CSVList
        self.list = CSV_List(self)
        self.merge_button = Button(self, text="Merge", command=self.load)

    def render(self):
        self.handle_load_button()
        self.pack(expand=True, fill='both')

    def load(self):
        try:
            print("Loading...")
            DatasetController.load()
            print("Merging...")
            DatasetController.merge()
            messagebox.showinfo("Success", "Successfully Loaded & Merged Dataset(s)")
            print("Done")
            self.navigate()
        except Exception as e:
            messagebox.showerror("Error", f'Error in Loading Dataset(s): {str(e)}')

    def navigate(self):
        analysis_frame: AnalysisFrame = self.master.winfo_children()[2]
        analysis_frame.table.setup()
        # Navigate to analysis frame
        self.master.select(analysis_frame)

    def handle_load_button(self):
        if len(API.csv.selected) > 0:
            self.merge_button.pack(anchor='s')
        else:
            self.merge_button.pack_forget()
