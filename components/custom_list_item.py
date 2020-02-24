from PyQt5.QtWidgets import QListWidgetItem


class CustomListItem(QListWidgetItem):
    def text(self):
        return self.param

    def __init__(self, param, *__args):
        super().__init__(*__args)
        self.param = param