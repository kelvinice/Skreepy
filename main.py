import sys

from PyQt5.QtWidgets import QApplication

from general.connection import Connection
from general.util import load_setting
from ui.main_window import MainWindow
from ui.report_history_window import ReportHistoryWindow


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        width = app.desktop().screenGeometry().width()
        height = app.desktop().screenGeometry().height()

        a = Connection().get_tests()  # Initializing database connection
        load_setting()  # Load Setting from config
        w = MainWindow(width, height, "Skreepy")
        w.setVisible(True)



        # m = MasterReportWindow(a,w)

        r = ReportHistoryWindow(w)
        r.setVisible(True)
        sys.exit(app.exec_())


if __name__ == '__main__':
    Main()

