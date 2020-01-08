import sys

from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from util.connection import Connection
from util.util import load_setting


def init():
    app = QApplication(sys.argv)
    width = app.desktop().screenGeometry().width()
    height = app.desktop().screenGeometry().height()

    Connection()  # Initializing database connection
    load_setting()  # Load Setting from config
    w = MainWindow(width, height, "Skreepy")
    w.setVisible(True)

    # print(super_global.expected)




    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
    # scraper.main.legacy_main()
