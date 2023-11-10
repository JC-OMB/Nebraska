import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import sqlite3

# Variables globales
df = None  # DataFrame para almacenar los datos cargados

# Función para cargar CSV
def cargar_csv():
    global df
    filepath = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not filepath:  # Si no se selecciona ningún archivo, no hacer nada
        return
    try:
        df = pd.read_csv(filepath)
        messagebox.showinfo("Cargar CSV", "Archivo cargado con éxito")
    except Exception as e:
        messagebox.showerror("Error al leer el archivo", str(e))

# Función para procesar datos
def procesar_datos():
    global df
    if df is None:
        messagebox.showerror("Procesar Datos", "No hay datos para procesar. Cargue un archivo CSV primero.")
        return
    try:
        # Aquí irían los filtros y el procesamiento de datos
        # Por ejemplo, reemplazar NaN por 0 (esto es solo un ejemplo, modifícalo según tus necesidades)
        df.fillna(0, inplace=True)
        
        # Almacenar los datos en SQLite
        with sqlite3.connect('datos_temporales.db') as conn:
            df.to_sql('datos_procesados', conn, if_exists='replace', index=False)
        
        messagebox.showinfo("Procesar Datos", "Los datos han sido procesados y almacenados en la base de datos.")
    except Exception as e:
        messagebox.showerror("Error en el procesamiento de datos", str(e))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Análisis de Datos")

# Frame para la carga de CSV
frame_carga_csv = tk.Frame(root)
frame_carga_csv.pack(padx=10, pady=10)

btn_cargar_csv = tk.Button(frame_carga_csv, text="Cargar CSV", command=cargar_csv)
btn_cargar_csv.pack(side=tk.LEFT, padx=5, pady=5)

# Frame para el procesamiento de datos
frame_procesamiento = tk.Frame(root)
frame_procesamiento.pack(padx=10, pady=10)

btn_procesar_datos = tk.Button(frame_procesamiento, text="Procesar Datos", command=procesar_datos)
btn_procesar_datos.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
