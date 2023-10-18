from app.libs.UI.label import Label
from app.libs.UI.entry import Entry


class EntryRow:

    def __init__(self, parent, name: str):
        Label(parent, name)
        Entry(parent, name)
