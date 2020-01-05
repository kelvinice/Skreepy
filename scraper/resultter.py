from PyQt5.QtWidgets import *


def condition_message(condition):
    if condition: return "Success"
    return "Error"


class Result_displayer(QMainWindow):

    def __init__(self, url, expected, result, parent=None):
        super(Result_displayer, self).__init__(parent)
        layout = QVBoxLayout()
        urlBeforeLbl = QLabel("Url Before : " + url)
        all_condition = True
        self.tblForm = QTableWidget()

        self.tblForm.setRowCount(3)
        self.tblForm.setColumnCount(4)

        header = ("What", "Expected", "Result", "Condition")
        self.tblForm.setHorizontalHeaderLabels(header)

        self.tblForm.setItem(0, 0, QTableWidgetItem("Url"))
        if expected["url_after"] != None:
            self.tblForm.setItem(0, 1, QTableWidgetItem(expected["url_after"]))
            self.tblForm.setItem(0, 2, QTableWidgetItem(result["url_after"]))
            condition = result["url_after"] == expected["url_after"]
            self.tblForm.setItem(0, 3, QTableWidgetItem(condition_message(condition)))
            all_condition = all_condition and condition

        self.tblForm.setItem(1, 0, QTableWidgetItem("Text"))
        if expected["text_after"] != None:
            self.tblForm.setItem(1, 1, QTableWidgetItem(expected["text_after"]))
            self.tblForm.setItem(1, 2, QTableWidgetItem(str(result["text_found"])))
            condition = result["text_found"]
            self.tblForm.setItem(1, 3, QTableWidgetItem(condition_message(condition)))
            all_condition = all_condition and condition

        self.tblForm.setItem(2, 0, QTableWidgetItem("Element"))
        if expected["element_after"] != None:
            self.tblForm.setItem(2, 1, QTableWidgetItem(expected["element_after"]))
            self.tblForm.setItem(2, 2, QTableWidgetItem(str(result["element_found"])))
            condition = result["element_found"]
            self.tblForm.setItem(2, 3, QTableWidgetItem(condition_message(condition)))
            all_condition = all_condition and condition

        layout.addWidget(urlBeforeLbl)
        layout.addWidget(self.tblForm)
        layout.addWidget(QLabel("Tested with result : " + condition_message(all_condition)))

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.resize(450, 300)
        self.setWindowTitle("Result Displayer")
        self.statusBar().showMessage("Active")
