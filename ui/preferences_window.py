from PyQt5.QtWidgets import QDialog, QLineEdit, QGridLayout, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox

from util.superglobal import SuperGlobal


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
        if self.exUrlLbl.text() != "":
            SuperGlobal.expected["url_after"] = self.exUrlLbl.text()
        if self.exTextLbl.text() != "":
            SuperGlobal.expected["text_after"] = self.exTextLbl.text()
        if self.exElementLbl.text() != "":
            SuperGlobal.expected["element_after"] = self.exElementLbl.text()

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)

        msg_box.setText("Preferences saved")
        msg_box.setWindowTitle("Save Success")
        # msgBox.setDetailedText("The details are as follows:")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.buttonClicked.connect(msgbtn)
        return_value = msg_box.exec()
        # if return_value == QMessageBox.Ok:
        #     print('OK clicked')
        self.close()


    def __init__(self, width, height, parent):
        super(PreferencesWindow, self).__init__(parent)
        self.resize(width, height)
        self.move((width / 2) / 2, (height / 2) / 2)
        self.setWindowTitle("Preferences")

        v_box = QVBoxLayout()
        self.exUrlLbl = QLineEdit()
        self.exTextLbl = QLineEdit()
        self.exElementLbl = QLineEdit()

        v_box.addWidget(wrap_layout_into_widget(wrap_text_edit_with_label(self.exUrlLbl, "Url Expected")))
        v_box.addWidget(wrap_layout_into_widget(wrap_text_edit_with_label(self.exTextLbl, "Text Expected")))
        v_box.addWidget(wrap_layout_into_widget(wrap_text_edit_with_label(self.exElementLbl, "Element Expected")))

        btn_save = QPushButton("Save")
        v_box.addWidget(btn_save)

        self.setLayout(v_box)

        btn_save.clicked.connect(self.save_click)





def msgbtn(i):
    if i.text() == "OK":
        pass






