import sys

from PyQt5.QtWidgets import QApplication

from general.connection import Connection
from general.util import load_setting, load_url
from ui.alternate_report_result_window import AlternateReportResultWindow
from ui.main_window import MainWindow
from ui.report_history_window import ReportHistoryWindow


class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        width = app.desktop().screenGeometry().width()
        height = app.desktop().screenGeometry().height()

        Connection()  # Initializing database connection
        load_setting()  # Load Setting from config
        load_url()  # Load URL List from json file
        w = MainWindow(width, height, "Skreepy")
        w.setVisible(True)

        sys.exit(app.exec_())


if __name__ == '__main__':
    Main()

