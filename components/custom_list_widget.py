from PyQt5.QtWidgets import QListWidget, QMessageBox, QListWidgetItem

from components.custom_list_item import CustomListItem


class CustomListWidget(QListWidget):
    # def clicked(self, item):
    #     QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())

    def set_item_list(self, list_item):
        for item in list_item:
            self.addItem(item)

    def addItem(self, item):
        super().addItem(CustomListItem(item["url"], item["name"]))

    def __init__(self):
        super(CustomListWidget, self).__init__(None)
        self.setMinimumHeight(400)


        self.setStyleSheet(
            """
            QListWidget{
                font-size:20px;
                background-color: white;
                margin-bottom: 20px;
                border-radius : 5px;
            }
            """
        )
        # self.itemClicked.connect(self.clicked)
