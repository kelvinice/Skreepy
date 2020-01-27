from functools import partial

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton

from general.connection import Connection
from ui.master_report_window import MasterReportWindow


class AlternateTable(QTableWidget):
    def click_report(self, args=0):
        report_list = Connection().get_tests(self.report_list[args]["id"])
        MasterReportWindow(report_list, self).show()

    def __init__(self, report_list, parent=None):
        super(AlternateTable, self).__init__(parent)
        self.report_list = report_list
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(1)
        header = ("Tester Name", "Title", "Date", "View")
        self.setHorizontalHeaderLabels(header)
        self.rowcount = 0
        self.setRowCount(len(self.report_list))
        self.setStyleSheet("color:black; background-color:white; }")
        for report in self.report_list:
            self.setItem(self.rowcount, 0, QTableWidgetItem(report["tester_name"]))
            self.setItem(self.rowcount, 1, QTableWidgetItem(report["test_title"]))
            self.setItem(self.rowcount, 2, QTableWidgetItem(report["test_date"]))

            input_button = QPushButton("View Alternate List")
            input_button.clicked.connect(partial(self.click_report, self.rowcount))
            self.setCellWidget(self.rowcount, 3, input_button)

            self.rowcount += 1
