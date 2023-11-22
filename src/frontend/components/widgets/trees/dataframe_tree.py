from tkinter.ttk import Treeview


class DataFrameWidget(Treeview):
    def __init__(self, master):
        super().__init__(master)
        self.api = master.api
        self.df = None

    def load(self, name):
        if self.df is not name:
            self.df = name
            self.setup()

    def setup(self):
        data = self.api.data.get(self.df)
        self['columns'] = list(data.columns)
        self['show'] = 'headings'
        for header in self['columns']:
            self.heading(header, text=header)
        for index, row in data.iterrows():
            self.insert('', 'end', values=list(row))

    def render(self):
        self.pack(fill='both', expand=1)
