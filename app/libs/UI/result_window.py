import tkinter as tk
from app.algorithms.function import f_rana
from app.algorithms.population import Population

from app.extensions import config
from app.libs.UI.button import Button
from app.calculate import Calculations
from app.graphing import Graphing

class ResultWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title(config.get('result_window', 'title'))
        self.geometry(config.get('result_window', 'width') + 'x' + config.get('result_window', 'height'))
        self.minsize(config.get('result_window', 'width'), config.get('result_window', 'height'))
        self.configure(
            background=config.get('color', 'primary'),
            padx=30,
            pady=20
        )

        self.calculate()

        Button(self, 'Plot graphs', self.show_graphs)
        Button(self, 'Close', self.close)

        self.mainloop()

    def calculate(self):
        self.add_label(f'Result found in {Calculations.algorithm_time} seconds')
        if Calculations.roulette_status:
            self.add_label(f'Results:\n y = {max(Calculations.data2export)}\n x1 = {Calculations.p} \n x2 = {Calculations.p}')
        else:
            self.add_label(f'Results:\n y = {min(Calculations.data2export)}\n x1 = {Calculations.p} \n x2 = {Calculations.p}')
        self.add_label(f'Ideal result = {f_rana([-488.662570, 512.0])}')


    def add_label(self, text):
        tk.Label(
            self,
            text=text,
            font=('Helvetica', 10),
            background=config.get('color', 'primary'),
            foreground=config.get('color', 'text')
        ).pack(expand=True)

    def show_graphs(self):
        Graphing.graph_results()
        self.destroy()

    def close(self):
        self.destroy()
