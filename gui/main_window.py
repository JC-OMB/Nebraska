import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from data.data_loader import DataLoader
from data.data_exporter import DataExporter
from database.db_manager import DatabaseManager
from gui.data_visualization import DataVisualization
import json
import os

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Análisis de Datos")
        self.root.geometry("800x600")

        self.data_loaders = {}
        self.db_managers = {}
        self.current_dataset = None

        self.data_visualization = DataVisualization(self.root)
        self.notebook = ttk.Notebook(self.root)

        self.home_frame = tk.Frame(self.notebook)
        self.data_frame = tk.Frame(self.notebook)
        self.visualization_frame = tk.Frame(self.notebook)
        self.export_frame = tk.Frame(self.notebook)

        self.notebook.add(self.home_frame, text='Home')
        self.notebook.add(self.data_frame, text='Data Loading & Processing')
        self.notebook.add(self.visualization_frame, text='Visualization')
        self.notebook.add(self.export_frame, text='Export')
        self.notebook.pack(expand=1, fill='both')

        self.setup_ui()

    def setup_ui(self):
        self.load_button_data = tk.Button(self.data_frame, text="Cargar CSV", command=self.load_csv)
        self.load_button_data.pack()

        self.dataset_selection = ttk.Combobox(self.data_frame, state="readonly", postcommand=self.update_dataset_selection)
        self.dataset_selection.pack()
        self.dataset_selection.bind("<<ComboboxSelected>>", self.on_dataset_selected)

        self.visualize_button_viz = tk.Button(self.visualization_frame, text="Visualizar Datos", command=self.visualize_data)
        self.visualize_button_viz.pack()

        self.column_selection = ttk.Combobox(self.visualization_frame)
        self.column_selection.pack()

        self.export_button_export = tk.Button(self.export_frame, text="Exportar Datos", command=self.export_data)
        self.export_button_export.pack()

        self.export_metadata_button = tk.Button(self.export_frame, text="Exportar Metadatos", command=self.export_metadata)
        self.export_metadata_button.pack()

    def load_csv(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filepath:
            try:
                data_loader = DataLoader()
                db_name = os.path.basename(filepath).split('.')[0] + '_temp_db.sqlite'
                db_manager = DatabaseManager(db_name)

                df = data_loader.load_csv(filepath)
                db_manager.save_data(df)

                self.data_loaders[filepath] = data_loader
                self.db_managers[filepath] = db_manager
                self.update_dataset_selection()

                messagebox.showinfo("Cargar CSV", "Archivo cargado con éxito")
            except Exception as e:
                messagebox.showerror("Error al leer el archivo", str(e))

    def update_dataset_selection(self):
        self.dataset_selection['values'] = list(self.data_loaders.keys())

    def on_dataset_selected(self, event=None):
        selected_file = self.dataset_selection.get()
        if selected_file:
            self.set_current_dataset(selected_file)
            self.column_selection['values'] = self.data_loaders[selected_file].df.columns.tolist()

    def set_current_dataset(self, dataset_name):
        self.current_dataset = dataset_name
        self.data_loader = self.data_loaders[dataset_name]
        self.db_manager = self.db_managers[dataset_name]

    def visualize_data(self):
        selected_column = self.column_selection.get()
        if not selected_column:
            messagebox.showwarning("Visualización", "Por favor, seleccione una columna para visualizar.")
            return
        df = self.db_manager.load_data()
        if df is None or df.empty:
            messagebox.showerror("Error", "No hay datos disponibles para visualizar.")
            return
        self.data_visualization.visualize_data(df, selected_column)



    def export_data(self):
        filepath = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if filepath:
            try:
                df = self.db_manager.load_data()
                data_exporter = DataExporter(df)
                data_exporter.export_csv(filepath)
                messagebox.showinfo("Exportar Datos", "Datos exportados con éxito en formato CSV.")
            except Exception as e:
                messagebox.showerror("Error en la exportación de datos", str(e))


    def export_metadata(self):
        metadata = {
            "fecha": "2023-11-13",
            "usuario": "nombre_usuario",
            "nombre_proyecto": "Proyecto X",
            "otros_datos": "Información adicional"
        }

        filepath = filedialog.asksaveasfilename(defaultextension='.json',
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filepath:
            data_exporter = DataExporter(None)
            data_exporter.export_json(filepath, metadata)
            messagebox.showinfo("Exportar Metadatos", "Metadatos exportados con éxito en formato JSON.")

