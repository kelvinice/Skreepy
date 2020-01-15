import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from general.connection import Connection
from general.util import load_setting


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        width = app.desktop().screenGeometry().width()
        height = app.desktop().screenGeometry().height()

        Connection()  # Initializing database connection
        load_setting()  # Load Setting from config
        w = MainWindow(width, height, "Skreepy")
        w.setVisible(True)

        sys.exit(app.exec_())


if __name__ == '__main__':
    Main()
