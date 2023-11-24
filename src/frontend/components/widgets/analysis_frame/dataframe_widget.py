from tkinter.ttk import Treeview

from api.api import API


class DataFrameWidget(Treeview):
    def __init__(self, master):
        super().__init__(master)
        # Get API
        self.df = None

    def load(self, name):
        if self.df is not name:
            self.df = name
            self.setup()

    def setup(self):
        data = API.data.get_data(self.df)
        self['columns'] = list(data.columns)
        self['show'] = 'headings'
        for header in self['columns']:
            self.heading(header, text=header)
        for index, row in data.iterrows():
            self.insert('', 'end', values=list(row))
        self.pack(fill='both', expand=1)
