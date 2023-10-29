import tkinter as tk
from app.calculate import Calculations

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
        Calculations.run_calculations(
            range_start=int(config.get('entries', 'start range')),
            range_end=int(config.get('entries', 'end range')),
            epoch=int(config.get('entries', 'epochs amount')),
            population_size=int(config.get('entries', 'population amount')),
            precision=float(config.get('entries', 'precision amount')),
            elite_strategy=float(config.get('entries', 'elite strategy percent')),
            cross_probability=float(config.get('entries', 'cross probability')),
            mutation_probability=float(config.get('entries', 'mutation probability')),
            inversion_probability=float(config.get('entries', 'inversion probability')),
            selection_method=str(config.get('options.best', 'chosen')),
            percent=float(config.get('entries', 'best and tournament chromosome amount')),
            tournament=float(config.get('entries', 'best and tournament chromosome amount')),
            cross_method=str(config.get('options.cross', 'chosen')),
            mutation_method=str(config.get('options.mutation', 'chosen')),
            roulette_status=config.get('checkboxes', 'max'),
            real=config.get('checkboxes', 'real')
            )
        ResultWindow()
