from functools import partial

import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton

from scraper.scraper import find_all_input, find_all_button, find_all_textarea, getheader, find_all_form


class InputResultTable(QTableWidget):
    def __init__(self,  url, result, parent=None):
        super(InputResultTable, self).__init__(parent)
        # pass

        self.url = url
        self.listofinputed = []

        # self.setRowCount(2)
        self.setColumnCount(6)
        # find_all_input(result)
        print(result)

        # header = ("Type", "Id", "Name", "Value", "Action", "Inner")
        # self.setHorizontalHeaderLabels(header)
        # self.setItem(0, 0, QTableWidgetItem(""))
        # # self.setItem(0, 1, "Ini Type")
        # # self.setItem(0, 2, "Ini Type")
        # # self.setItem(0, 3, "Ini Type")
        # # self.setItem(0, 4, "Ini Type")
        # # self.setItem(0, 5, "Ini Type")

        # self.inputs = find_all_input(result)
                      # + find_all_button(result) + find_all_textarea(result)
        # self.setRowCount(len(self.inputs))

        # self.rowcount = 0
        # for inp in self.inputs:
        #     header = getheader(inp)
        #     if header["innerHTML"] != None and header["innerHTML"].lower() == "submit":
        #         itemtype = QTableWidgetItem(header["innerHTML"])
        #     else:
        #         itemtype = QTableWidgetItem(header["type"])
        #     itemid = QTableWidgetItem(header["id"])
        #     itemname = QTableWidgetItem(header["name"])
        #     iteminner = QTableWidgetItem(header["innerHTML"])
        #
        #     itemtype.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        #     itemid.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        #     itemname.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
        #
        #     self.setItem(self.rowcount, 0, itemtype)
        #     self.setItem(self.rowcount, 1, itemid)
        #     self.setItem(self.rowcount, 2, itemname)
        #     self.setItem(self.rowcount, 3, QTableWidgetItem(header["value"]))
        #     self.setItem(self.rowcount, 4, iteminner)
        #     input_button = QPushButton("Click")
        #     # input_button.clicked.connect(partial(self.on_click, self.rowcount))
        #     self.setCellWidget(self.rowcount, 4, input_button)
        #
        #     self.rowcount += 1

        # self.cellChanged.connect(self.cellChanged)

