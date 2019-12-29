import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.report_window import ReportWindow
from faker import Faker
import scraper.main

############################################
def init():
    app = QApplication(sys.argv)
    width = app.desktop().screenGeometry().width()
    height = app.desktop().screenGeometry().height()
    # fake = Faker()
    # print(fake.address())
    w = MainWindow(width, height, "Skreepy")
    w.setVisible(True)
    from util.super_global import super_global

    print(super_global.expected)

    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
    #scraper.main.legacy_main()

