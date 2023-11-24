from tkinter.ttk import Treeview

from api.api import API


class DataFrameWidget(Treeview):
    def __init__(self, master):
        super().__init__(master)
        # Setup
        self.setup()
        # Render
        self.render()

    def setup(self):
        try:
            self.dataset = API.data.get("universal")
            self['columns'] = list(self.dataset.columns)
            self['show'] = 'headings'
            for header in self['columns']:
                self.heading(header, text=header)
            for index, row in self.dataset.iterrows():
                self.insert('', 'end', values=list(row))
        except Exception as e:
            print(f'Error Retrieving Dataset: {e}')

    def render(self):
        self.pack(fill='both', expand=1)
