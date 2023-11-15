import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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

        self.setup_ui()

    def setup_ui(self):
        # Example UI setup - you'll need to expand this with your specific components
        self.load_button = tk.Button(self.root, text="Cargar CSV", command=self.load_csv)
        self.load_button.pack()

        self.visualize_button = tk.Button(self.root, text="Visualizar Datos", command=self.visualize_data)
        self.visualize_button.pack()

        self.export_button = tk.Button(self.root, text="Exportar Datos", command=self.export_data)
        self.export_button.pack()

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
