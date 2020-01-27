from functools import partial

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton

from general.util import get_overall_result
from ui.report_window import ReportWindow


class MasterReportTable(QTableWidget):
    def click_report(self, args=0):
        print(self.report_list[args])
        ReportWindow(800, 680, data=self.report_list[args], parent=self).show()

    def __init__(self, report_list, parent=None):
        super(MasterReportTable, self).__init__(parent)
        self.report_list = report_list
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(3)
        header = ("Test ID", "Date", "Overall Result", "Action")
        self.setHorizontalHeaderLabels(header)
        self.rowcount = 0
        self.setRowCount(len(report_list))
        self.setStyleSheet("color:black; background-color:white; }")
        for report in report_list:
            self.setItem(self.rowcount, 0, QTableWidgetItem(report["id"]))
            self.setItem(self.rowcount, 1, QTableWidgetItem(report["date"]))
            overall_result = get_overall_result(report["expected"], report["result"])
            self.setItem(self.rowcount, 2, QTableWidgetItem(str(overall_result)))

            input_button = QPushButton("View Report")
            input_button.clicked.connect(partial(self.click_report, self.rowcount))
            self.setCellWidget(self.rowcount, 3, input_button)

            self.rowcount += 1
