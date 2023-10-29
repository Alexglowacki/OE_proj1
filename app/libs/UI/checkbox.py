import tkinter as tk

from app.extensions import config


class Checkbox(tk.Checkbutton):

    def __init__(self, parent, name):
        self.name = name
        self.intVar = tk.IntVar()
        self.intVar.trace('w', self.callback)
        super().__init__(
            parent,
            text=str.capitalize(name),
            variable=self.intVar,
            onvalue=1,
            offvalue=0,
            anchor=tk.W,
            justify=tk.LEFT,
            font=('Helvetica', 10),
            pady=4,
            background=config.get('color', 'primary'),
            foreground=config.get('color', 'text'),
            selectcolor=config.get('color', 'secondary'),
            activebackground='black',
            activeforeground=config.get('color', 'text')
        )

        self.pack(fill=tk.X)

    def callback(self, *args):
        config.set('checkboxes', self.name, self.intVar.get())
