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
            # Load Dataset
            self.dataset = API.data.get("universal")
            # Visualize Dataset as Plot
            # TODO - Allow the user to select the x and y axis with Comboboxes
            self.x = 'startDateTime'
            self.y = 'tempSingleMean'
            #
            self.render_graph()
        except Exception as e:
            print(f'Error Visualizing Dataset: {e}')

    def update_selection(self):
        # ...
        # TODO - Update the user's selection the x and y axis from the Comboboxes
        self.x = 'startDateTime'
        self.y = 'tempSingleMean'
        self.render_graph()

    def render(self):
        self.pack(expand=True, fill='both')

    def render_graph(self):
        # TODO (Optional) - Allow the user to select the type of plot
        self.fig, self.ax = plt.subplots()
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        widget = canvas.get_tk_widget()
        self.ax.plot(self.dataset[self.x], self.dataset[self.y])
        self.ax.set_xlabel(self.x)
        self.ax.set_ylabel(self.y)
        widget.pack(fill="both", expand=True)

# Usage example
# root = tk.Tk()
# visualization_frame = VisualizationFrame(root)
# root.mainloop()
