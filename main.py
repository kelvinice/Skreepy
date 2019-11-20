import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.report_window import ReportWindow
from faker import Faker

############################################
def init():
    app = QApplication(sys.argv)
    width = app.desktop().screenGeometry().width()
    height = app.desktop().screenGeometry().height()
    # fake = Faker()
    # print(fake.address())
    w = MainWindow(width, height, "Main Window")
    sys.exit(app.exec_())


if __name__ == '__main__':
    init()
