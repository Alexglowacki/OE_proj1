import tkinter as tk

from app.extensions import config


class Label(tk.Label):

    def __init__(self, parent, name):
        super().__init__(
            parent,
            text=str.capitalize(name),
            anchor=tk.W,
            justify=tk.LEFT,
            font=('Helvetica', 10),
            pady=2,
            bg=config.get('color', 'primary'),
            fg=config.get('color', 'text')
        )

        self.pack(fill=tk.X)
