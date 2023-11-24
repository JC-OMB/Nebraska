from tkinter import Frame, Button, messagebox

from api.api import API
from frontend.components.widgets.analysis_frame.analysis_frame import AnalysisFrame
from frontend.components.widgets.files_frame.csv_list.csv_list import CSV_List
from frontend.components.widgets.files_frame.schemas_list.schemas_list import SchemasList


class FilesFrame(Frame):
    _instance = None
    label = "Data Loading"

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(FilesFrame, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Create widgets
            self.add_widgets()
            # Initial Render
            self.render()

    def add_widgets(self):
        self.schemas_list = SchemasList(self)
        self.csv_list = CSV_List(self)
        self.add_button = Button(self, text="Add CSV(s)", command=self.csv_list.add_rows)
        self.load_button = Button(self, text="Load Dataset(s)", command=self.load_rows)

    def load_rows(self):
        if API.csv.selected:
            API.data.load_all()
            messagebox.showinfo("Load Datasets", "Files loaded successfully")
            self.navigate()
        else:
            messagebox.showerror(title="Error", message="Error: No files selected")

    def navigate(self):
        analysis_frame: AnalysisFrame = self.master.winfo_children()[2]
        analysis_frame.update_combobox()
        # Navigate to analysis frame
        self.master.select(analysis_frame)

    def render(self):
        self.schemas_list.render()
        self.csv_list.render()
        self.render_add_button()
        self.render_load_button()

    def render_add_button(self):
        self.add_button.pack_forget()
        if len(API.csv.sources) < 4:
            self.add_button.pack(anchor='center')

    def render_load_button(self):
        self.load_button.pack_forget()
        if len(API.csv.selected) > 0:
            self.load_button.pack(anchor='s')
