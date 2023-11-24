import json
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Variables globales
df = None  # DatasetFrame para almacenar los datos cargados


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
        df.columns = [col.strip().rstrip(',') for col in df.columns]
        combo_columnas['values'] = df.columns.tolist()
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
        with sqlite3.connect('datos_temporales.csv') as conn:
            df.to_sql('datos_procesados', conn, if_exists='replace', index=False)
        messagebox.showinfo("Procesar Datos", "Los datos han sido procesados y almacenados.")
    except Exception as e:
        messagebox.showerror("Error en el procesamiento de datos", str(e))


# Función para visualizar datos
def visualizar_datos():
    try:
        columna_seleccionada = combo_columnas.get()
        if not columna_seleccionada:
            messagebox.showwarning("Visualización", "Por favor, seleccione una columna para visualizar.")
            return

        conn = sqlite3.connect('datos_temporales.csv')
        df = pd.read_sql_query("SELECT * FROM datos_procesados", conn)
        conn.close()

        if df.empty:
            messagebox.showwarning("Visualización", "No hay datos para visualizar.")
            return

        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df[columna_seleccionada], label=f'{columna_seleccionada}')
        plt.xlabel('Índice')
        plt.ylabel(columna_seleccionada)
        plt.title(f'{columna_seleccionada} a lo largo del tiempo')
        plt.legend()

        fig = plt.gcf()

        # Crear un frame para cada gráfico en el frame interno
        frame_grafico = tk.Frame(frame_interno)
        frame_grafico.pack(fill=tk.BOTH, expand=True)

        # Mostrar el gráfico en un canvas de Matplotlib dentro del frame
        canvas_matplotlib = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas_matplotlib.draw()
        widget_canvas = canvas_matplotlib.get_tk_widget()
        widget_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Crear un botón para cerrar el gráfico
        btn_cerrar_grafico = tk.Button(frame_grafico, text="Cerrar Gráfico", command=lambda: frame_grafico.destroy())
        btn_cerrar_grafico.pack(side=tk.TOP)
    except Exception as e:
        messagebox.showerror("Error en la visualización", str(e))


# Función para exportar datos
def exportar_datos():
    try:
        conn = sqlite3.connect('datos_temporales.csv')
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
root.geometry("800x600")

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

# Frame para seleccionar columna
frame_seleccion_columna = tk.Frame(root)
frame_seleccion_columna.pack(padx=10, pady=10)

label_seleccion_columna = tk.Label(frame_seleccion_columna, text="Seleccionar Columna:")
label_seleccion_columna.pack(side=tk.LEFT, padx=5, pady=5)

combo_columnas = ttk.Combobox(frame_seleccion_columna)
combo_columnas.pack(side=tk.LEFT, padx=5, pady=5)

# Crear un frame contenedor para el canvas y las barras de desplazamiento
frame_contenedor = tk.Frame(root)
frame_contenedor.pack(fill=tk.BOTH, expand=True)

# Crear un canvas dentro del frame contenedor
canvas = tk.Canvas(frame_contenedor)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Crear barras de desplazamiento
scrollbar_y = tk.Scrollbar(frame_contenedor, orient="vertical", command=canvas.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = tk.Scrollbar(frame_contenedor, orient="horizontal", command=canvas.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# Configurar el canvas para usar las barras de desplazamiento
canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Crear un frame interno dentro del canvas para colocar los contenidos
frame_interno = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_interno, anchor='nw')


def on_frame_configure(event):
    # Actualizar el área de desplazamiento para cubrir el frame interno
    canvas.configure(scrollregion=canvas.bbox("all"))


frame_interno.bind("<Configure>", on_frame_configure)

# Botones para visualizar y exportar datos
btn_visualizar_datos = tk.Button(root, text="Visualizar Datos", command=visualizar_datos)
btn_visualizar_datos.pack()

btn_exportar_datos = tk.Button(root, text="Exportar Datos", command=exportar_datos)
btn_exportar_datos.pack()

btn_exportar_metadatos = tk.Button(root, text="Exportar Metadatos", command=exportar_metadatos)
btn_exportar_metadatos.pack()

root.mainloop()
