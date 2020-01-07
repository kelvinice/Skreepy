from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QLabel
from PyQt5.uic.uiparser import QtWidgets

from scraper.resultter import condition_message


class ResultReportTable(QTableWidget):
    def __init__(self, expected, result, parent=None):
        super(ResultReportTable, self).__init__(parent)

        self.all_condition = True
        header = ("Parameter", "Expected", "Result", "Condition")


        self.setRowCount(3)
        self.setColumnCount(4)
        self.horizontalHeader().setSectionResizeMode(3)

        self.setHorizontalHeaderLabels(header)
        self.setItem(0, 0, QTableWidgetItem("Url"))
        # print(result)
        if expected["url_after"] is not None:
            self.setItem(0, 1, QTableWidgetItem(expected["url_after"]))
            self.setItem(0, 2, QTableWidgetItem(result["url_after"]))
            condition = result["url_after"] == expected["url_after"]
            self.setItem(0, 3, QTableWidgetItem(condition_message(condition)))
            self.all_condition = self.all_condition and condition

        self.setItem(1, 0, QTableWidgetItem("Text"))
        if expected["text_after"] is not None:
            self.setItem(1, 1, QTableWidgetItem(expected["text_after"]))
            self.setItem(1, 2, QTableWidgetItem(str(result["text_found"])))
            condition = result["text_found"]
            self.setItem(1, 3, QTableWidgetItem(condition_message(condition)))
            self.all_condition = self.all_condition and condition

        self.setItem(2, 0, QTableWidgetItem("Element"))
        if expected["element_after"] is not None:
            self.setItem(2, 1, QTableWidgetItem(expected["element_after"]))
            self.setItem(2, 2, QTableWidgetItem(str(result["element_found"])))
            condition = result["element_found"]
            self.setItem(2, 3, QTableWidgetItem(condition_message(condition)))
            self.all_condition = self.all_condition and condition


    def get_condition_label(self):
        if self.all_condition:
            result = QLabel("SUCCESS")
            result.setStyleSheet("color : green;")
        else:
            result = QLabel("FAILED")
            result.setStyleSheet("color : red;")
        return result

    def save_all(self):
        pass

    def get_overall_result(self):
        return self.all_condition
