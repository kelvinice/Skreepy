from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QScrollArea, QLineEdit, QGroupBox, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, QSize
from PyQt5 import QtCore, QtGui


####################################
class MainWindow(QWidget):

    def __init__(self, width, height, title):
        super(MainWindow, self).__init__()
        self.move(0, 0)
        self.resize(width, height)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("assets/logoBINUS.png"))
        self.setStyleSheet("background-color : #242423")

        self.top_group_box = QGroupBox("Scrapper")
        self.toolbar_group_box = QGroupBox("Menu Bar")
        self.main_h_layout = QGroupBox()

        self.init_toolbar_attribute()
        self.init_top_attribute()
        self.init_bottom_attribute()

        v_box = QVBoxLayout()
        v_box.addWidget(self.top_group_box)
        v_box.addWidget(self.toolbar_group_box)
        v_box.addWidget(self.main_h_layout)

        self.setLayout(v_box)
        self.showMaximized()

    def init_toolbar_attribute(self):
        self.toolbar_group_box.setStyleSheet(
            "color: white;"
            "font-size: 20px;"
        )
        toolbar_h_box_layout = QHBoxLayout()
        toolbar_h_box_layout.setGeometry(QRect(0, 0, 0, 0))
        toolbar_h_box_layout.setAlignment(QtCore.Qt.AlignLeft)
        prev_button = QPushButton()
        home_button = QPushButton()
        report_button = QPushButton()
        prev_button.setIcon(QIcon("assets/prev.png"))
        prev_button.setStyleSheet("""
                    QPushButton
                    {
                        background-color: #5b5c5e;
                        padding: 2px;
                        min-height: 45px;
                        min-width: 45px;
                        border-radius: 10px;
                        border-bottom: 1.5px solid black;
                        border-right: 1px solid black;
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
        prev_button.setIconSize(QSize(40, 40))

        home_button.setIcon(QIcon("assets/home.png"))
        home_button.setStyleSheet("""
                    QPushButton
                    {
                        background-color: #5b5c5e;
                        padding: 2px;
                        min-height: 45px;
                        min-width: 45px;
                        border-radius: 10px;
                        border-bottom: 1.5px solid black;
                        border-right: 1px solid black;
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
        home_button.setIconSize(QSize(40, 40))

        report_button.setIcon(QIcon("assets/report.png"))
        report_button.setStyleSheet("""
                    QPushButton
                    {
                        background-color: #5b5c5e;
                        padding: 2px;
                        min-height: 45px;
                        min-width: 45px;
                        border-radius: 10px;
                        border-bottom: 1.5px solid black;
                        border-right: 1px solid black;
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
        report_button.setIconSize(QSize(40, 40))
        toolbar_h_box_layout.addWidget(prev_button)
        toolbar_h_box_layout.addWidget(home_button)
        toolbar_h_box_layout.addWidget(report_button)
        self.toolbar_group_box.setLayout(toolbar_h_box_layout)

    def init_top_attribute(self):
        self.top_group_box.setStyleSheet("color: white;"
                                         "font-size: 20px;")
        top_h_box_layout = QHBoxLayout()
        get_forms_button = QPushButton("Get Form")
        get_forms_button.setGeometry(QRect(0, 0, 150, 150))
        get_forms_button.setMinimumHeight(20)
        get_forms_button.setStyleSheet("""
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
        url_line_edit = QLineEdit()
        url_line_edit.setStyleSheet("""
                QLineEdit
                {
                    border-radius: 5px; 
                    width: 300px;
                    color:black;
                    height: 30px;
                    background-color: white;
                }
                QLineEdit:focus
                {
                    border-bottom : 0.5px solid grey;
                    border-right : 1px solid grey;
                }
        """)
        top_h_box_layout.addWidget(url_line_edit)
        top_h_box_layout.addWidget(get_forms_button)
        self.top_group_box.setLayout(top_h_box_layout)

    def init_bottom_attribute(self):
        main_h_layout = QGridLayout()
        box_left = QGroupBox()
        box_right = QGroupBox()
        left_v_layout = QVBoxLayout()
        right_v_layout = QVBoxLayout()

        url_scroll_area = QScrollArea()
        url_scroll_area.setStyleSheet("""
            QScrollArea{
                background-color: white;
                margin-bottom: 20px;
                border-radius : 5px;
            }
        """)
        button_save_url = QPushButton("Save URL")
        button_save_url.setStyleSheet("""
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
        left_v_layout.addWidget(url_scroll_area)
        left_v_layout.addWidget(button_save_url)

        box_left.setLayout(left_v_layout)
        main_scroll_area = QScrollArea()
        main_scroll_area.setStyleSheet("""
            QScrollArea
            {
                background-color : white;
                border-radius: 5px;
            }
            
        """)
        right_v_layout.addWidget(main_scroll_area)
        box_right.setLayout(right_v_layout)

        main_h_layout.addWidget(box_left, 0, 0)
        main_h_layout.addWidget(box_right, 0, 1)
        main_h_layout.setColumnStretch(1, 1)

        self.main_h_layout.setLayout(main_h_layout)