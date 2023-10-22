import tkinter as tk

from app.extensions import config


class Button(tk.Button):

    def __init__(self, parent, name):
        # self.string_var = tk.StringVar()
        # self.string_var.trace('w', self.callback)
        super().__init__(
            parent,
            font=('Helvetica', 10),
            text='Click',
            bg=config.get('color', 'secondary'),
            fg=config.get('color', 'text'),
            highlightthickness=0.5,
        )
        self.name = name

        self.pack(ipady=2, fill=tk.X)

    def callback(self, *args):
        config.set('buttons', self.name)
        print(config.get('buttons', self.name))
