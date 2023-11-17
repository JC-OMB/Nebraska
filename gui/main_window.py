import tkinter as tk
from tkinter import ttk, filedialog, messagebox
# Assuming the below imports are correct and the modules are available
from data.data_loader import DataLoader
from data.data_exporter import DataExporter
from database.db_manager import DatabaseManager
from gui.data_visualization import DataVisualization

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Análisis de Datos")
        self.root.geometry("800x600")

        self.data_loader = DataLoader()
        self.db_manager = DatabaseManager('datos_temporales.db')
        self.data_visualization = DataVisualization(root)
        self.notebook = ttk.Notebook(self.root)

        # Home tab
        self.home_frame = tk.Frame(self.notebook)
        self.notebook.add(self.home_frame, text='Home')
        
        # Data loading & processing tab
        self.data_frame = tk.Frame(self.notebook)
        self.load_button_data = tk.Button(self.data_frame, text="Cargar CSV", command=self.load_csv)
        self.load_button_data.pack()
        self.notebook.add(self.data_frame, text='Data Loading & Processing')

        # Visualization tab
        self.visualization_frame = tk.Frame(self.notebook)
        self.visualize_button_viz = tk.Button(self.visualization_frame, text="Visualizar Datos", command=self.visualize_data)
        self.visualize_button_viz.pack()
        self.notebook.add(self.visualization_frame, text='Visualization')

        # Export tab
        self.export_frame = tk.Frame(self.notebook)
        self.export_button_export = tk.Button(self.export_frame, text="Exportar Datos", command=self.export_data)
        self.export_button_export.pack()
        self.notebook.add(self.export_frame, text='Export')

        self.notebook.pack(expand=1, fill='both')

        self.setup_ui()

    def setup_ui(self):
        # UI components in the home_frame
        self.load_button_home = tk.Button(self.home_frame, text="Cargar CSV", command=self.load_csv)
        self.load_button_home.pack()

        self.visualize_button_home = tk.Button(self.home_frame, text="Visualizar Datos", command=self.visualize_data)
        self.visualize_button_home.pack()

        self.export_button_home = tk.Button(self.home_frame, text="Exportar Datos", command=self.export_data)
        self.export_button_home.pack()

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filepath:
            try:
                self.data_loader.load_csv(filepath)
                messagebox.showinfo("Cargar CSV", "Archivo cargado con éxito")
            except Exception as e:
                messagebox.showerror("Error al leer el archivo", str(e))

    def visualize_data(self):
        # Call visualization method from DataVisualization class
        pass

    def export_data(self):
        # Call export method from DataExporter class
        pass