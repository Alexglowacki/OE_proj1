import tkinter as tk

from app.extensions import config


class Option(tk.OptionMenu):

    def __init__(self, parent, name):
        self.name = name
        self.string_var = tk.StringVar()
        self.string_var.set(config.get(name, 'chosen'))
        self.string_var.trace('w', self.callback)
        super().__init__(parent, self.string_var, *config.get(name, 'options').split(','))
        self.configure(
            background=config.get('color', 'secondary'),
            foreground=config.get('color', 'text'),
            activebackground=config.get('color', 'tertiary'),
            activeforeground=config.get('color', 'text')
        )

        self.pack(fill=tk.X)

    def callback(self, *args):
        config.set(self.name, 'chosen', self.string_var.get())
