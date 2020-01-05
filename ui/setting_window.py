from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class SettingWindow(QMainWindow):
    def __init__(self,width, height, parent):
        super(SettingWindow, self).__init__(parent)
        self.resize(width / 2, height / 2)
        self.setWindowTitle("Setting")
        self.setWindowIcon(QIcon("assets/logoBINUS.png"))
        self.setStyleSheet("background-color : #949494;"
                           "color: white;")