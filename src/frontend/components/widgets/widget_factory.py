from enum import Enum

from frontend.components.widgets.frames import *


class WidgetFactory:
    class Widgets(Enum):
        MainNotebook = [HomeFrame, FilesFrame, AnalysisFrame, VisualizationFrame, ExportFrame]

    @staticmethod
    def get_widgets(instance):
        class_name = instance.__class__.__name__
        widgets = WidgetFactory.Widgets[class_name]
        return widgets.value
