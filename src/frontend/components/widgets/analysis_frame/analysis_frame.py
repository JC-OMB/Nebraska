from tkinter import Frame, Button

from frontend.components.widgets.analysis_frame.dataframe_widget import DataFrameWidget
from frontend.components.widgets.visualization_frame.visualization_frame import VisualizationFrame


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
            self.add_widgets()
            # Render
            self.render()

    def add_widgets(self):
        self.table = DataFrameWidget(self)
        self.merge_button = Button(self, text="Visualize", command=self.navigate)

    def navigate(self):
        visualization_frame: VisualizationFrame = self.master.winfo_children()[3]
        visualization_frame.setup()
        # Navigate to analysis frame
        self.master.select(3)

    def render(self):
        self.merge_button.pack(anchor='n')
        self.pack(expand=True, fill='both')
