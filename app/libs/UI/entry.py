import tkinter as tk

from app.extensions import config


class Entry(tk.Entry):

    def __init__(self, parent, name):
        self.string_var = tk.StringVar()
        self.string_var.trace('w', self.callback)
        super().__init__(
            parent,
            textvariable=self.string_var,
            font=('Helvetica', 10),
            insertbackground='white',
            bg=config.get('color', 'secondary'),
            fg=config.get('color', 'text'),
            highlightthickness=0.5,
        )
        self.name = name

        self.pack(ipady=2, fill=tk.X)

    def callback(self, *args):
        config.set('entries', self.name, self.string_var.get())
        print(config.get('entries', self.name))
