from email import header

from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLabel, QGroupBox, QPushButton, QFormLayout, \
    QTableWidget, QScrollArea, QGridLayout, QWidget, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from components.result_report_table import ResultReportTable
from util.connection import Connection


class ReportWindow(QDialog):
    def __init__(self, width, height, data, parent):
        super(ReportWindow, self).__init__(parent)
        self.resize(width, height)
        self.move((width / 2) / 2, (height / 2) / 2)
        self.setWindowTitle("Report " + data["title"])
        self.setWindowIcon(QIcon("assets/report.png"))
        self.setStyleSheet("background-color :  #949494;")
        self.box_title = QGroupBox()
        self.box_header = QGroupBox("Description")
        self.box_table = QScrollArea()
        self.box_result = QGroupBox()
        self.data = data

        self.init_title_description()
        self.init_main_table(data["expected"], data["result"])
        self.init_result()

        v_box = QVBoxLayout()
        v_box.addWidget(self.box_title)
        v_box.addWidget(self.box_header)
        v_box.addWidget(self.box_table)
        v_box.addWidget(self.box_result)

        self.setLayout(v_box)
        self.show()

    def init_title_description(self):
        title = QLabel("Report of test " + self.data["title"])
        title.setStyleSheet("""
            QLabel
            {
                color : white;
                font-family: Candara, Calibri, Segoe, "Segoe UI", Optima, Arial, sans-serif; 
                font-size: 24px;
            }
        """)
        title.setAlignment(QtCore.Qt.AlignCenter)
        h_title_layout = QHBoxLayout()
        h_title_layout.addWidget(title)
        self.box_title.setLayout(h_title_layout)

        form_layout = QFormLayout()
        label_test_id = QLabel("Test ID")
        test_id = QLabel(self.data['id'])
        label_date = QLabel("Date")
        date = QLabel(self.data["date"])
        label_test_name = QLabel("Test Name")
        name = QLabel(self.data["title"])
        label_tester = QLabel("Tester")

        tester = QLabel(self.data["tester"])
        form_layout.addRow(label_test_id, test_id)
        form_layout.addRow(label_date, date)
        form_layout.addRow(label_test_name, name)
        form_layout.addRow(label_tester, tester)
        self.box_header.setStyleSheet("""
            QGroupBox
            {
                color: white;
                font-size : 17px;
            }
            QLabel
            {
                color: white;
                font-size : 15px;
            }
        """)
        self.box_header.setLayout(form_layout)

    def init_main_table(self, expected, result):
        pass
        h_box = QHBoxLayout()
        self.main_table = ResultReportTable(expected=expected, result=result, parent=self)
        self.data["overall_result"] = self.main_table.get_overall_result()
        h_box.addWidget(self.main_table)
        self.box_table.setLayout(h_box)

    def init_result(self):
        self.box_result.setStyleSheet("""
            QGroupBox
            {
                color: white;
                font-size : 17px;
            }
            QLabel
            {
                color: white;
                font-size : 15px;
            }
        """)

        form_box = QGroupBox()
        form_layout = QFormLayout()
        form_box.setStyleSheet("border: none;")
        label_result = QLabel("Overall Result : ")
        result = self.main_table.get_condition_label()
        form_layout.addRow(label_result, result)
        form_box.setLayout(form_layout)

        label_additional_desc = QLabel("Additional Description")
        scroll_area_description = QScrollArea()
        description_text_edit = QTextEdit()
        description_text_edit.setText(self.data["description"])
        description_text_edit.setStyleSheet("""
                    QTextEdit
                    {
                        color: black;
                        font-size : 14px;
                    }
                    """)

        # scroll_area_description.setWidget(description_text_edit)

        scroll_area_description.setStyleSheet("background: white;")
        button_save = QPushButton("Save Test Result")
        generate_button = QPushButton("Generate Test Result")

        button_save.clicked.connect(self.click_save)

        v_box = QGridLayout()
        v_box.addWidget(form_box, 0, 0)
        v_box.addWidget(label_additional_desc, 1, 0)
        v_box.addWidget(description_text_edit, 2, 0)
        v_box.addWidget(button_save, 3, 0)
        v_box.addWidget(generate_button, 3, 1)
        self.box_result.setStyleSheet("""
            QPushButton
            {
                background-color: #5b5c5e;
                color: white;
                border-radius: 10px;
                border-bottom: 1.5px solid black;
                border-right: 1px solid black;
                padding: 10px;
                font-size: 15px;
            }   
            QPushButton:hover:!pressed
                {
                  background-color: #4d4d4d;
                }
            QPushButton:pressed
                {
                  background-color: #5b5c5e;
                  border: 1px solid black;
                }
        """)
        self.box_result.setLayout(v_box)

    def click_save(self):
        conn = Connection()
        conn.insert_test(self.data)
