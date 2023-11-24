from tkinter import Frame, Button, messagebox

from api.api import API


class ExportFrame(Frame):
    _instance = None
    label = "Export"

    def __new__(cls, master):
        if cls._instance is None:
            cls._instance = super(ExportFrame, cls).__new__(cls)
            cls._instance.initialized = False
        return cls._instance

    def __init__(self, master):
        if not self.initialized:
            # Initialize
            super().__init__(master)
            self.initialized = True
            # Add widgets
            self.add_widgets()
            # Render
            self.render()

    def add_widgets(self):
        # download button
        self.export_button = Button(self, text="Export Merged Dataset", command=self.export)

    def render(self):
        # download button
        self.export_button.pack(side="top")
        self.pack(fill="both", expand=True)

    def export(self):
        try:
            print("Exporting...")
            API.data.export()
            messagebox.showinfo("Success", "Successfully Exported Merged Dataset(s) to Desktop")
            print("Done")
        except Exception as e:
            messagebox.showerror("Error", f'Error in Loading Dataset(s): {str(e)}')
