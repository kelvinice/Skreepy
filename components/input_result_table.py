from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class InputResultTable(QTableWidget):
    def __init__(self):
        super(InputResultTable, self).__init__()

        # pass

        # self.url = url
        # self.listofinputed = []
        # self.inputs = result
        # self.tblForm = QTableWidget()

        self.setRowCount(2)
        self.setColumnCount(6)

        header = ("Type", "Id", "Name", "Value", "Action", "Inner")
        self.setHorizontalHeaderLabels(header)
        self.setItem(0, 0, QTableWidgetItem(""))
        # self.setItem(0, 1, "Ini Type")
        # self.setItem(0, 2, "Ini Type")
        # self.setItem(0, 3, "Ini Type")
        # self.setItem(0, 4, "Ini Type")
        # self.setItem(0, 5, "Ini Type")

