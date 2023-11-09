import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Esta función se llamará cuando el usuario haga clic en el botón "Cargar CSV"
def cargar_csv():
    # Abrir el diálogo de selección de archivos y obtener la ruta del archivo
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if not filepath:  # Si no se selecciona ningún archivo, no hacer nada
        return
    try:
        # Leer el archivo CSV con pandas y posiblemente almacenarlo en alguna estructura
        df = pd.read_csv(filepath)
        # Aquí puedes añadir el dataframe a una lista o directamente a una base de datos
        print(df)  # Solo para fines de depuración, mostrar el dataframe en la consola
    except Exception as e:
        tk.messagebox.showerror("Error al leer el archivo", str(e))
        return

# Configuración de la ventana principal y el botón de carga
root = tk.Tk()
root.title("Aplicación de Análisis de Datos")

frame_carga_csv = tk.Frame(root)
frame_carga_csv.pack(padx=10, pady=10)

btn_cargar_csv = tk.Button(frame_carga_csv, text="Cargar CSV", command=cargar_csv)
btn_cargar_csv.pack()

root.mainloop()
