import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.report_window import ReportWindow
from faker import Faker
import scraper.main


############################################
from util.util import get_today


def init():
    app = QApplication(sys.argv)
    width = app.desktop().screenGeometry().width()
    height = app.desktop().screenGeometry().height()

    # fake = Faker()
    # print(fake.address())
    w = MainWindow(width, height, "Skreepy")
    w.setVisible(True)

    print(get_today())

    from util.superglobal import SuperGlobal

    # print(super_global.expected)

    # Initializing database connection
    from util.connection import Connection
    # Connection()

    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
    # scraper.main.legacy_main()
