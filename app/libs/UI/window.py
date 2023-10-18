import tkinter as tk

from app.extensions import config
from app.libs.UI.entry_row import EntryRow
from app.libs.UI.option_row import OptionRow


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(config.get('window', 'title'))
        self.geometry(config.get('window', 'width') + 'x' + config.get('window', 'height'))
        self.minsize(config.get('window', 'width'), config.get('window', 'height'))
        self.configure(background=config.get('color', 'primary'), padx=30, pady=20)

        for row in dict(config.items('entries')):
            EntryRow(self, row)

        for row in config.get('options', 'options').split(','):
            OptionRow(self, row)
