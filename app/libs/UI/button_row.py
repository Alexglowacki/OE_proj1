from app.libs.UI.label import Label
from app.libs.UI.button import Button


class ButtonRow:

    def __init__(self, parent, name: str):
        Label(parent, name)
        Button(parent, name)