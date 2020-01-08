from PyQt5.QtWidgets import QDialog, QLineEdit, QGridLayout, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, \
    QFormLayout

from util.superglobal import SuperGlobal
from util.util import save_setting


def wrap_layout_into_widget(layout):
    widget = QWidget()
    widget.setLayout(layout)
    return widget


def wrap_text_edit_with_label(q_line_edit, text):
    grid_layout = QGridLayout()
    grid_layout.setColumnStretch(1, 2)
    label = QLabel(text)
    grid_layout.addWidget(label)
    grid_layout.addWidget(q_line_edit)
    return grid_layout


class PreferencesWindow(QDialog):
    def save_click(self):
        print(SuperGlobal.setting["expected"])
        if self.exUrlLbl.text() != "":
            SuperGlobal.setting["expected"]["url_after"] = self.exUrlLbl.text()
        if self.exTextLbl.text() != "":
            SuperGlobal.setting["expected"]["text_after"] = self.exTextLbl.text()
        if self.exElementLbl.text() != "":
            SuperGlobal.setting["expected"]["element_after"] = self.exElementLbl.text()

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)

        msg_box.setText("Preferences saved")
        msg_box.setWindowTitle("Save Success")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.buttonClicked.connect(msgbtn)
        return_value = msg_box.exec()
        save_setting()
        # if return_value == QMessageBox.Ok:
        #     print('OK clicked')
        self.close()

    def __init__(self, width, height, parent):
        super(PreferencesWindow, self).__init__(parent)
        self.resize(width, height)
        self.move((width / 2), (height / 2))
        self.setWindowTitle("Preferences")

        master = QVBoxLayout();
        v_box = QFormLayout()
        self.exUrlLbl = QLineEdit()
        self.exTextLbl = QLineEdit()
        self.exElementLbl = QLineEdit()

        self.exUrlLbl.setText(SuperGlobal.setting["expected"]["url_after"])
        self.exTextLbl.setText(SuperGlobal.setting["expected"]["text_after"])
        self.exElementLbl.setText(SuperGlobal.setting["expected"]["element_after"])

        v_box.addRow("Url Expected", self.exUrlLbl)
        v_box.addRow("Text Expected", self.exTextLbl)
        v_box.addRow("Element Expected", self.exElementLbl)

        btn_save = QPushButton("Save")

        master.addWidget(wrap_layout_into_widget(v_box))
        master.addWidget(btn_save)
        self.setLayout(master)

        btn_save.clicked.connect(self.save_click)
        self.setStyleSheet("""
        QLabel{
            font-size: 18px;
        }
        QLineEdit{
            font-size: 16px;
        }
        QPushButton{
            padding: 5px;
            font-size: 20px;
        }
        """)


def msgbtn(i):
    if i.text() == "OK":
        pass
