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

    import requests
    #


    # session = requests.Session()
    # headers = {"User-Agent": UA}
    # q = session.get(url="https://www.tokopedia.com/", verify=False, headers=headers)
    # print(q)

    # fake = Faker()
    # print(fake.address())
    w = MainWindow(width, height, "Skreepy")
    w.setVisible(True)
    # w = ReportWindow(width, height, "Skreepy")
    # w.setVisible(True)
    from util.super_global import super_global

    # print(super_global.expected)

    # Initializing database connection
    from util.connection import Connection
    # Connection()

    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
    #scraper.main.legacy_main()

