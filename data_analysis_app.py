import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

# Función para cargar CSV
def cargar_csv():
    global df
    filepath = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    if not filepath:
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
        df.fillna(0, inplace=True)
        with sqlite3.connect('datos_temporales.db') as conn:
            df.to_sql('datos_procesados', conn, if_exists='replace', index=False)
        messagebox.showinfo("Procesar Datos", "Los datos han sido procesados y almacenados.")
    except Exception as e:
        messagebox.showerror("Error en el procesamiento de datos", str(e))

# Función para visualizar datos
def visualizar_datos():
    try:
        conn = sqlite3.connect('datos_temporales.db')
        df = pd.read_sql_query("SELECT * FROM datos_procesados", conn)
        conn.close()

        if df.empty:
            messagebox.showwarning("Visualización", "No hay datos para visualizar.")
            return

        plt.figure(figsize=(6, 4))
        # Aquí puedes modificar el gráfico según tus necesidades, AQUI SE MODIFICAN LOS DATOS A MOSTRAR
        
        plt.plot(df['surfWaterTempMean'])  # Ejemplo simple

        fig = plt.gcf()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
        canvas.draw()
    except Exception as e:
        messagebox.showerror("Error en la visualización", str(e))

# Función para exportar datos
def exportar_datos():
    try:
        conn = sqlite3.connect('datos_temporales.db')
        df = pd.read_sql_query("SELECT * FROM datos_procesados", conn)
        conn.close()

        filepath = filedialog.asksaveasfilename(defaultextension='.csv',
                                                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not filepath:
            return

        df.to_csv(filepath, index=False)
        messagebox.showinfo("Exportar Datos", "Datos exportados con éxito en formato CSV.")
    except Exception as e:
        messagebox.showerror("Error en la exportación de datos", str(e))

# Función para exportar metadatos
def exportar_metadatos():
    metadatos = {
        "fecha": "2023-11-13",
        "usuario": "nombre_usuario",
        "nombre_proyecto": "Proyecto X",
        "sensores": "Sensor1, Sensor2",
        "lugar": "Ubicación X"
    }

    filepath = filedialog.asksaveasfilename(defaultextension='.json',
                                            filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
    if not filepath:
        return

    with open(filepath, 'w') as f:
        json.dump(metadatos, f)

    messagebox.showinfo("Exportar Metadatos", "Metadatos exportados con éxito en formato JSON.")

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

# Botón para visualizar los datos
btn_visualizar_datos = tk.Button(root, text="Visualizar Datos", command=visualizar_datos)
btn_visualizar_datos.pack()

# Botón para exportar los datos
btn_exportar_datos = tk.Button(root, text="Exportar Datos", command=exportar_datos)
btn_exportar_datos.pack()

# Botón para exportar metadatos
btn_exportar_metadatos = tk.Button(root, text="Exportar Metadatos", command=exportar_metadatos)
btn_exportar_metadatos.pack()

root.mainloop()
