from PyQt5.QtWidgets import QDialog, QVBoxLayout, QScrollArea

from components.master_report_table import MasterReportTable
from general.connection import Connection


class ReportHistoryWindow(QDialog):
    def initialize_table(self):
        pass

    def __init__(self, parent):
        super(ReportHistoryWindow, self).__init__(parent)
        self.window_width = 800
        self.window_height = 600
        self.resize(self.window_width, self.window_height)
        self.move((self.window_width / 2) / 2, (self.window_height / 2) / 2)
        self.setStyleSheet("background-color :  #949494;")
        self.setWindowTitle("Report History")
        scroll = QScrollArea()
        scroll.setMinimumWidth(self.window_width)
        v_box = QVBoxLayout(self)
        inner = QVBoxLayout()

        report_list = Connection().get_tests()
        self.master_report_table = MasterReportTable(report_list, self)

        scroll.setLayout(inner)
        # scroll.setWidget()
        inner.addWidget(self.master_report_table)
        v_box.addWidget(scroll)

        self.setLayout(v_box)
        self.show()
