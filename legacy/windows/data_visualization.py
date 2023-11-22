import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DataVisualization:
    def __init__(self, root):
        self.root = root

    def visualize_data(self, data, column):
        if data is None or column not in data.columns:
            print("Error: El FilesFrame es None o la columna no existe.")
            return

        graph_window = tk.Toplevel(self.root)
        graph_window.title("Visualización de Datos")

        fig, ax = plt.subplots()
        ax.plot(data.index, data[column], label=column)
        ax.set_xlabel('Índice')
        ax.set_ylabel(column)
        ax.set_title(f'{column} a lo largo del tiempo')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
