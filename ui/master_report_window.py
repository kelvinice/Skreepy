from PyQt5.QtWidgets import QDialog, QVBoxLayout

from components.master_report_table import MasterReportTable


class MasterReportWindow(QDialog):
    def __init__(self, report_list, parent):
        super(MasterReportWindow, self).__init__(parent)
        self.window_width = 546
        self.window_height = 600
        self.resize(self.window_width, self.window_height)
        self.move((self.window_width / 2) / 2, (self.window_height / 2) / 2)
        self.setStyleSheet("background-color :  #949494;")
        v_box = QVBoxLayout()

        self.master_report_table = MasterReportTable(report_list, self)
        v_box.addWidget(self.master_report_table)

        self.setLayout(v_box)
        self.show()
