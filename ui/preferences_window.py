from PyQt5.QtWidgets import QDialog, QLineEdit, QGridLayout, QLabel, QWidget, QVBoxLayout, QPushButton, QMessageBox, \
    QFormLayout, QCheckBox

from general import util
from general.globalpreferences import GlobalPreferences
from general.util import save_setting


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
        GlobalPreferences.setting["expected"]["url_after"] = self.exUrlEdt.text()
        GlobalPreferences.setting["expected"]["text_after"] = self.exTextEdt.text()
        GlobalPreferences.setting["expected"]["element_after"] = self.exElementEdt.text()

        GlobalPreferences.setting["close_browser_after_test"] = self.closeBrowserChk.isChecked()
        try:
            GlobalPreferences.setting["timeout"] = int(self.timeoutEdt.text())
        except:
            util.show_message_window("Invalid Setting","Timeout must be a numeric")
            return
        GlobalPreferences.setting["tester"] = self.testerEdt.text()

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

        master = QVBoxLayout()
        v_box = QFormLayout()
        self.exUrlEdt = QLineEdit()
        self.exTextEdt = QLineEdit()
        self.exElementEdt = QLineEdit()
        self.closeBrowserChk = QCheckBox()
        self.timeoutEdt = QLineEdit()
        self.testerEdt = QLineEdit()

        self.exUrlEdt.setText(GlobalPreferences.setting["expected"]["url_after"])
        self.exTextEdt.setText(GlobalPreferences.setting["expected"]["text_after"])
        self.exElementEdt.setText(GlobalPreferences.setting["expected"]["element_after"])
        self.closeBrowserChk.setChecked(GlobalPreferences.setting["close_browser_after_test"])
        self.timeoutEdt.setText(str(GlobalPreferences.setting["timeout"]))
        self.testerEdt.setText(str(GlobalPreferences.setting["tester"]))

        v_box.addRow("Expected URL", self.exUrlEdt)
        v_box.addRow("Expected Text ", self.exTextEdt)
        v_box.addRow("Expected Element", self.exElementEdt)
        v_box.addRow("Close Browser After Test", self.closeBrowserChk)
        v_box.addRow("Time Out(seconds)", self.timeoutEdt)
        v_box.addRow("Tester", self.testerEdt)

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
        QCheckBox{
            spacing: 5px;
            font-size:25px;  
        }
        """)


def msgbtn(i):
    if i.text() == "OK":
        pass
