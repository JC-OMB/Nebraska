from tkinter.ttk import Frame

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from api.api import API


class GraphWidget(Frame):
    def __init__(self, master):
        super().__init__(master)
        # Setup
        self.setup()
        # Render
        self.render()

    def setup(self):
        try:
            self.dataset = API.data.get("universal")
            self.figure = plt.figure(figsize=(10, 10))
            self.axes = self.figure.add_subplot(111)
            self.axes.plot(self.dataset.index, self.dataset['startDateTime'])
            self.canvas = FigureCanvasTkAgg(self.figure, self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill='both', expand=1)
        except Exception as e:
            print(f'Error: {e}')

    def render(self):
        self.pack(fill='both', expand=1)
