import tkinter as tk

from app.extensions import config
from app.libs.UI.entry_row import EntryRow
from app.libs.UI.option_row import OptionRow
from app.libs.UI.checkbox import Checkbox
from app.libs.UI.button import Button
from app.libs.UI.result_window import ResultWindow


class Window(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(config.get('window', 'title'))
        self.geometry(config.get('window', 'width') + 'x' + config.get('window', 'height'))
        self.minsize(config.get('window', 'width'), config.get('window', 'height'))
        self.configure(background=config.get('color', 'primary'), padx=30, pady=20)

        for section in config.sections():
            if section.startswith('entries'):
                for entry in config.options(section):
                    EntryRow(self, entry)
            if section.startswith('options'):
                OptionRow(self, section)
            if section.startswith('checkboxes'):
                for checkbox in config.options(section):
                    Checkbox(self, checkbox)

        Button(self, 'Submit', self.open)

    def open(self):
        self.destroy()

        ResultWindow()
