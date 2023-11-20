from pathlib import Path
from tkinter import filedialog, Frame, Button, BooleanVar, Checkbutton

class FilesFrame(Frame):
    label = "Data Loading & Processing"

    def __init__(self, master):
        super().__init__(master)
        # Set up data
        self.db = master.db
        # Create widgets
        self.add_widgets()
        # Render
        self.render()

    def add_widgets(self):
        self.paths_list = Frame(self)
        self.paths_list.pack(anchor='n', fill='x')

        self.add_button = Button(self, text="Add CSV(s)", command=self.add_rows)
        self.add_button.pack(anchor='center')

        self.load_button = Button(self, text="Load CSV(s)", command=self.load_rows)
        self.load_button.pack(anchor='s')

    def add_row(self, path):
        row_frame = Frame(self.paths_list)

        label = path.stem
        selection = BooleanVar(value=path in self.db.selected_csv_paths)
        command = lambda: self.select_row(path, selection)
        checkbox = Checkbutton(row_frame, text=label, var=selection, command=command)
        checkbox.pack(side='left')

        remove_btn = Button(row_frame, text="Remove", fg="red", command=lambda p=path: self.remove_row(p))
        remove_btn.pack(side='right')

        row_frame.pack(anchor='n', fill='x')

    def add_rows(self):
        # Get CSV paths
        paths = filedialog.askopenfilenames(title="Open CSV files", filetypes=[("CSV files", "*.csv")])
        # Convert paths to Path objects
        paths = [Path(path) for path in paths]
        # Add CSV paths to database
        self.db.add_csvs(paths)
        # Render rows
        self.render_rows()

    def load_rows(self):
        self.db.load_csvs()
        # TODO: Add loading indicator
        # TODO: Add success indicator

    def remove_row(self, path):
        self.db.remove_csv(path)
        self.render_rows()

    def render(self):
        self.toggle_paths_list()
        self.toggle_add_button()
        self.toggle_load_button()

    def render_rows(self):
        # Destroy Rows
        [row.destroy() for row in self.paths_list.winfo_children()]
        # Render Rows
        for path in self.db.csv_paths:
            self.add_row(path)
        # Toggle Buttons
        self.render()

    def select_row(self, path, selection):
        is_selected = selection.get()
        if is_selected:
            self.db.selected_csv_paths.add(path)
        else:
            self.db.selected_csv_paths.discard(path)
        self.render_rows()

    def toggle_paths_list(self):
        self.paths_list.pack_forget()
        if self.db.csv_paths:
            self.paths_list.pack(anchor='n', fill='x')

    def toggle_add_button(self):
        self.add_button.pack_forget()
        if len(self.db.csv_paths) < 4:
            self.add_button.pack(anchor='center')

    def toggle_load_button(self):
        self.load_button.pack_forget()
        if len(self.db.selected_csv_paths) > 0:
            self.load_button.pack(anchor='s')