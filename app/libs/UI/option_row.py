from app.libs.UI.label import Label
from app.libs.UI.option import Option


class OptionRow:

    def __init__(self, parent, name):
        Label(parent, name.split('.')[1] + ' strategy')
        Option(parent, name)
