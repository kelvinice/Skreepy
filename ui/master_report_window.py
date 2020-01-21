from PyQt5.QtWidgets import QDialog, QVBoxLayout

from components.master_report_table import MasterReportTable


class MasterReportWindow(QDialog):
    def __init__(self, width, height, report_list, parent):
        super(MasterReportWindow, self).__init__(parent)
        self.resize(width, height)
        self.move((width / 2) / 2, (height / 2) / 2)
        self.setStyleSheet("background-color :  #949494;")
        v_box = QVBoxLayout()

        self.master_report_table = MasterReportTable(report_list, self)
        v_box.addWidget(self.master_report_table)

        self.setLayout(v_box)
        self.show()
