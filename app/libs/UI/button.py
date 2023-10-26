import tkinter as tk

from app.extensions import config


class Button(tk.Button):

    def __init__(self, parent, name, callback):
        super().__init__(
            parent,
            text=name,
            font=('Helvetica', 10),
            pady=4,
            background=config.get('color', 'secondary'),
            foreground=config.get('color', 'text'),
            activebackground=config.get('color', 'tertiary'),
            activeforeground=config.get('color', 'text'),
            command=callback
        )

        self.pack(fill=tk.X)
