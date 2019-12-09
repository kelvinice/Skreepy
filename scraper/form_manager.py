from functools import partial

import PyQt5.QtWidgets

import main
import scraper.automator
import scraper.input_manager


class form_manager(PyQt5.QtWidgets.QMainWindow):
    def on_click(self, args=0):

        if self.comboAuto.currentText() == "Manual":
            dialog = scraper.input_manager.input_manager(url=self.url, result=self.forms[int(args)], parent=self)
            dialog.show()
        elif self.comboAuto.currentText() == "Automated":
            scraper.automator.Automator(url=self.url, result=self.forms[int(args)])

    def __init__(self, url, result, parent=None):
        super(form_manager, self).__init__(parent)
        self.url = url
        self.tblForm = PyQt5.QtWidgets.QTableWidget()

        from scraper.scraper import getheader, find_all_form

        self.forms = find_all_form(result)
        self.tblForm.setRowCount(len(self.forms))

        self.tblForm.setColumnCount(3)

        header = ("Method", "Action", "Event")
        self.tblForm.setHorizontalHeaderLabels(header)

        self.rowcount = 0
        for f in self.forms:
            header = getheader(f)
            methoditem = PyQt5.QtWidgets.QTableWidgetItem(header["method"])

            self.tblForm.setItem(self.rowcount, 0, methoditem)
            self.tblForm.setItem(self.rowcount, 1, PyQt5.QtWidgets.QTableWidgetItem(header["action"]))
            button = PyQt5.QtWidgets.QPushButton("Input", self)

            curr = self.rowcount
            button.clicked.connect(partial(self.on_click, curr))
            self.tblForm.setCellWidget(self.rowcount, 2, button)
            # self.tblForm.setCellWidget(self.rowcount, 3, comboAuto)
            self.rowcount += 1

        layout = PyQt5.QtWidgets.QVBoxLayout()
        layout.addWidget(self.tblForm)

        # TODO refactor
        self.comboAuto = PyQt5.QtWidgets.QComboBox()
        self.comboAuto.addItem("Manual")
        self.comboAuto.addItem("Automated")

        gridAction = PyQt5.QtWidgets.QGridLayout()
        gridAction.setColumnStretch(1, 2)
        gridAction.addWidget(PyQt5.QtWidgets.QLabel("Type of Action"))
        gridAction.addWidget(self.comboAuto)

        leftright = PyQt5.QtWidgets.QWidget()
        leftright.setLayout(gridAction)
        layout.addWidget(leftright)

        central = PyQt5.QtWidgets.QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.resize(450, 300)
        self.setWindowTitle("Form Manager")
        self.statusBar().showMessage("Active")


if __name__ == "__main__":
    main.main()
