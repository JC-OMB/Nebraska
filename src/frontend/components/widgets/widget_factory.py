from enum import Enum

from frontend.components.widgets.analysis_frame.analysis_frame import AnalysisFrame
from frontend.components.widgets.export_frame.export_frame import ExportFrame
from frontend.components.widgets.files_frame.files_frame import FilesFrame
from frontend.components.widgets.home_frame.home_frame import HomeFrame
from src.frontend.components.widgets.visualization_frame.visualization_frame import VisualizationFrame


class WidgetFactory:
    class Widgets(Enum):
        MainNotebook = [HomeFrame, FilesFrame, AnalysisFrame, VisualizationFrame, ExportFrame]

    @staticmethod
    def get(cls):
        class_name = cls.__name__
        widgets = WidgetFactory.Widgets[class_name]
        return widgets.value
