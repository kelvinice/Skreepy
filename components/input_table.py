import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class InputTable(QTableWidget):
    def insert_data(self, data):
        rowPosition = self.rowCount()
        self.insertRow(rowPosition)
        itemtype = QTableWidgetItem(data["tag"])
        itemid = QTableWidgetItem(data["id"])
        itemname = QTableWidgetItem(data["name"])
        itemhtml = QTableWidgetItem(data["innerHTML"])
        item_original_value = QTableWidgetItem(data["original_value"])
        itemtype.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        itemid.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        itemname.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        self.setItem(rowPosition, 0, itemtype)
        self.setItem(rowPosition, 1, itemid)
        self.setItem(rowPosition, 2, itemname)
        self.setItem(rowPosition, 3, itemhtml)
        self.setItem(rowPosition, 4, item_original_value)
        self.setItem(rowPosition, 5, QTableWidgetItem(data["value"]))


    def __init__(self, input_list, parent=None):
        super(InputTable, self).__init__(parent)

        self.setColumnCount(6)

        header = ("Tag", "Id", "Name", "innerHTML", "Original Value", "Value")
        self.setHorizontalHeaderLabels(header)
        self.setRowCount(len(input_list))
        self.horizontalHeader().setSectionResizeMode(1)
        self.rowcount = 0
        for inp in input_list:
            itemtype = QTableWidgetItem(inp["tag"])
            itemid = QTableWidgetItem(inp["id"])
            itemname = QTableWidgetItem(inp["name"])
            itemhtml = QTableWidgetItem(inp["innerHTML"])
            item_original_value = QTableWidgetItem(inp["original_value"])
            itemtype.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemid.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemname.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            self.setItem(self.rowcount, 0, itemtype)
            self.setItem(self.rowcount, 1, itemid)
            self.setItem(self.rowcount, 2, itemname)
            self.setItem(self.rowcount, 3, itemhtml)
            self.setItem(self.rowcount, 4, item_original_value)
            self.setItem(self.rowcount, 5, QTableWidgetItem(inp["value"]))

            self.rowcount += 1
