import matplotlib

matplotlib.use('TkAgg')
from tkinter import Frame
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from api.api import API


class VisualizationFrame(Frame):
    label = "Visualization"

    def __init__(self, master):
        super().__init__(master)
        self.render()

    def setup(self):
        try:
            df = API.data.get("universal")
            self.fig, self.ax = plt.subplots()
            canvas = FigureCanvasTkAgg(self.fig, master=self)
            widget = canvas.get_tk_widget()
            x = 'startDateTime'
            y = 'tempSingleMean'
            self.ax.plot(df[x], df[y])
            self.ax.set_xlabel(x)
            self.ax.set_ylabel(y)
            widget.pack(fill="both", expand=True)
        except Exception as e:
            print(f'Error Visualizing Dataset: {e}')

    def render(self):
        self.pack(expand=True, fill='both')

# Usage example
# root = tk.Tk()
# visualization_frame = VisualizationFrame(root)
# root.mainloop()
