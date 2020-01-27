import sys
from functools import partial

import PyQt5
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QScrollArea, QLineEdit, QGridLayout

from components.input_result_table import InputResultTable
from components.input_table import InputTable
from scraper.scraper import getheader, find_all_form
from ui.preferences_window import PreferencesWindow
from ui.report_history_window import ReportHistoryWindow


class MainWindow(QMainWindow):

    def __init__(self, width, height, title):
        super(MainWindow, self).__init__()
        self.resize(width, height)
        self.showMaximized()
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon("assets/logoBINUS.png"))
        self.setStyleSheet("background-color : #949494;")

        self.input_result_table = None
        self.default_url_text = "https://industry.socs.binus.ac.id/learning-plan/auth/login"

        self.top_group_box = QGroupBox("Scrapper")
        self.toolbar_group_box = QGroupBox("Menu Bar")
        self.action_group_box = QGroupBox("Action")
        self.main_h_layout = QGroupBox()

        # self.init_menu_bar()
        self.init_toolbar_attribute()
        self.init_top_attribute()
        self.init_bottom_attribute()
        self.init_action_attribute()

        v_box = QVBoxLayout()
        h_box = QHBoxLayout()
        h_box.addWidget(self.toolbar_group_box)
        h_box.addWidget(self.action_group_box)
        h_wid = QWidget()
        h_wid.setLayout(h_box)

        v_box.addWidget(self.top_group_box)
        v_box.addWidget(h_wid)
        v_box.addWidget(self.main_h_layout)

        widget = QWidget()
        widget.setLayout(v_box)
        self.setCentralWidget(widget)

        # datas = Connection().get_tests()
        # for data in datas:
        #     export_to_html(data)
        # o = ReportWindow(800, 680, data=data, parent=self)
        # o.setVisible(True)

    def execute_click(self):
        if self.input_result_table is not None:
            self.input_result_table.execute_all_click()

    def execute_alter(self):
        if self.input_result_table is not None:
            self.input_result_table.execute_alternate()

    def open_preferences(self):
        p = PreferencesWindow(600, 180, self)
        p.show()

    def open_history_report(self):
        r = ReportHistoryWindow(self)
        r.setVisible(True)

    def init_menu_bar(self):
        menu_bar = self.menuBar()
        setting_menu = menu_bar.addMenu("Settings")
        change_user_action = QAction(QIcon("assets/user.png"), 'Change User', self)
        exit_button = QAction(QIcon("assets/exit.png"), 'Exit', self)
        preferences_button = QAction(QIcon("assets/exit.png"), 'Preferences', self)
        setting_menu.triggered[QAction].connect(self.setting_listener)
        exit_button.triggered.connect(self.close)
        preferences_button.triggered.connect(self.open_preferences)

        setting_menu.addAction(change_user_action)
        setting_menu.addAction(preferences_button)
        setting_menu.addAction(exit_button)

    def init_action_attribute(self):
        action_h_box_layout = QHBoxLayout()
        action_h_box_layout.setGeometry(QRect(0, 0, 0, 0))
        action_h_box_layout.setAlignment(QtCore.Qt.AlignRight)
        self.action_group_box.setStyleSheet(
            "color: white;"
            "font-size: 20px;"
        )

        execute_button = QPushButton("Execute")
        execute_alternative_scenario_button = QPushButton("Execute with Alternative Scenario")
        execute_button.setStyleSheet("""
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



        execute_alternative_scenario_button.setStyleSheet("""
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

        execute_button.clicked.connect(self.execute_click)
        execute_alternative_scenario_button.clicked.connect(self.execute_alter)

        action_h_box_layout.addWidget(execute_button)
        action_h_box_layout.addWidget(execute_alternative_scenario_button)
        self.action_group_box.setLayout(action_h_box_layout)

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
        setting_button = QPushButton()
        setting_button.setIcon(QIcon("assets/setting.png"))
        setting_button.setStyleSheet("""
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
        setting_button.setIconSize(QSize(40, 40))

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
        report_button.clicked.connect(self.open_history_report)

        setting_button.clicked.connect(self.open_preferences)

        # toolbar_h_box_layout.addWidget(prev_button)
        toolbar_h_box_layout.addWidget(home_button)
        toolbar_h_box_layout.addWidget(report_button)
        toolbar_h_box_layout.addWidget(setting_button)
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
        self.url_line_edit = QLineEdit()
        self.url_line_edit.setText(self.default_url_text)
        self.url_line_edit.setStyleSheet("""
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
        top_h_box_layout.addWidget(self.url_line_edit)
        top_h_box_layout.addWidget(get_forms_button)
        self.top_group_box.setLayout(top_h_box_layout)
        get_forms_button.clicked.connect(self.click_insert_form_result)

    def init_bottom_attribute(self):
        main_h_layout = QGridLayout()
        box_left = QGroupBox()
        box_right = QGroupBox()
        left_v_layout = QVBoxLayout()
        self.right_v_layout = QVBoxLayout()

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

        box_right.setLayout(self.right_v_layout)

        main_h_layout.addWidget(box_left, 0, 0)
        main_h_layout.addWidget(box_right, 0, 1)
        main_h_layout.setColumnStretch(1, 1)

        self.main_h_layout.setLayout(main_h_layout)

    def setting_listener(self, q):
        if q.text() == "Change User":
            print("Change User")
            return
        if q.text() == "Exit":
            sys.exit()
            return

        return

    def click_insert_form_result(self):
        self.url = self.url_line_edit.text()

        from scraper.scraper import scrape
        self.result = scrape(self.url)

        self.forms = find_all_form(self.result)

        self.tblForm = PyQt5.QtWidgets.QTableWidget()
        self.tblForm.setRowCount(len(self.forms))

        self.tblForm.setColumnCount(3)

        header = ("Method", "Action", "Event")
        self.tblForm.setHorizontalHeaderLabels(header)
        self.tblForm.horizontalHeader().setSectionResizeMode(3)

        self.rowcount = 0

        self.main_scroll_widged = QWidget()
        self.main_scroll_vbox = QVBoxLayout()

        header = ("Method", "Action", "Event")
        self.tblForm.setHorizontalHeaderLabels(header)

        rowcount = 0

        for f in self.forms:
            header = getheader(f)
            methoditem = PyQt5.QtWidgets.QTableWidgetItem(header["method"])

            self.tblForm.setItem(self.rowcount, 0, methoditem)
            self.tblForm.setItem(self.rowcount, 1, PyQt5.QtWidgets.QTableWidgetItem(header["action"]))
            button = PyQt5.QtWidgets.QPushButton("Input", self)

            curr = self.rowcount
            button.clicked.connect(partial(self.click_insert_input_result, curr))
            self.tblForm.setCellWidget(self.rowcount, 2, button)
            rowcount += 1

        self.main_scroll_vbox.addWidget(self.tblForm)
        self.main_scroll_widged.setLayout(self.main_scroll_vbox)

        self.right_v_layout.addWidget(self.main_scroll_widged)

    def click_insert_input_result(self, args=0):
        self.tblForm.setParent(None)

        self.input_result_table = InputResultTable(self.url, self.forms[int(args)], self)
        self.input_table = InputTable([], self)

        self.main_scroll_vbox.addWidget(self.input_result_table)
        self.main_scroll_vbox.addWidget(self.input_table)

        # self.main_scroll_vbox.addWidget()
        # dialog = scraper.input_manager.input_manager(url=self.url, result=self.forms[int(args)], parent=self)
        # dialog.show()

    def set_input_table(self, data):
        self.input_table.insert_data(data)
