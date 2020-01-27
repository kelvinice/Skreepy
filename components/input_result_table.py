from functools import partial

import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from general import util
from general.combination import Combination
from general.globalpreferences import GlobalPreferences
from general.util import get_today, get_uuid, normalize_string
from scraper.scraper import find_all_input, find_all_button, find_all_textarea, getheader, Scraper
from ui.master_report_window import MasterReportWindow


class InputResultTable(QTableWidget):
    def execute_alternate(self):
        input_combinations = Combination(data_set=self.list_of_input).get_result_reversed()
        master_data = []
        for com in input_combinations:
            description = ""
            scr = Scraper()
            browser = scr.dive_plus(self.url, com)
            wait = WebDriverWait(browser, GlobalPreferences.setting["timeout"])
            try:
                page_loaded = wait.until_not(
                    lambda browser: browser.current_url == self.url
                )
            except TimeoutException:
                print("Timeout")
                description = "Timeout\n"
            finally:
                result = {
                    "url_after": browser.current_url,
                    "text_found": scr.find_text_in_browser(GlobalPreferences.setting["expected"]["text_after"]),
                    "element_found": scr.find_element_in_browser(GlobalPreferences.setting["expected"]["element_after"])
                }
                data = {
                    "result": result,
                    "expected": GlobalPreferences.setting["expected"],
                    "id": str(get_uuid()),
                    "date": get_today(),
                    "title": "Skreepy",
                    "description": description,
                    "tester": GlobalPreferences.setting["tester"],
                    "inputs": com,
                    "master_test_id": normalize_string(util.get_uuid())
                }
                master_data.append(data)
                browser.close()
        MasterReportWindow(master_data, self).show()

    def execute_all_click(self):
        print("executed")
        description = ""

        from scraper import scraper
        scraper.browser = scraper.dive_plus(self.url, self.list_of_input)

        wait = WebDriverWait(scraper.browser, GlobalPreferences.setting["timeout"])
        try:
            page_loaded = wait.until_not(
                lambda browser: browser.current_url == self.url
            )
            print("Page is ready!")
            cookies = scraper.browser.get_cookies()

            for cookie in cookies:
                print(cookie['name'], " : ", cookie['value'])
                scraper.session.cookies.set(cookie['name'], cookie['value'])

            # loginResult = scraper.scrape(self.expected["url_after"])
            # self.browser_shower.setText(str(loginResult))
        except TimeoutException:
            print("Timeout")
            description = "Timeout\n"
        finally:
            result = {
                "url_after": scraper.browser.current_url,
                "text_found": scraper.find_text(GlobalPreferences.setting["expected"]["text_after"]),
                "element_found": scraper.find_element(GlobalPreferences.setting["expected"]["element_after"])
            }
            data = {
                "result": result,
                "expected": GlobalPreferences.setting["expected"],
                "id": str(get_uuid()),
                "date": get_today(),
                "title": "Skreepy",
                "description": description,
                "tester": GlobalPreferences.setting["tester"],
                "inputs": self.list_of_input,
                "master_test_id": ""
            }
            if GlobalPreferences.setting["close_browser_after_test"]:
                scraper.browser.close()
            from ui.report_window import ReportWindow
            o = ReportWindow(800, 680, data=data, parent=self)
            o.setVisible(True)

    def cell_changed_reaction(self, row, col):

        # Value changed
        if col == 3:
            print("Value Change To : " + str(self.item(row, col).text()))
            from scraper import scraper
            text = str(self.item(row, col).text())
            data = {"tag": scraper.getheader(self.inputs[row])["tag"], "id": scraper.getheader(self.inputs[row])["id"],
                 "class": scraper.getheader(self.inputs[row])["class"],
                 "name": scraper.getheader(self.inputs[row])["name"], "value": text,
                 "innerHTML": scraper.getheader(self.inputs[row])["innerHTML"],
                 "original_value": scraper.getheader(self.inputs[row])["value"],
                 }
            self.list_of_input.append(data)
            self.parentWindow.set_input_table(data)

    def on_click(self, args=0):
        # TODO VALIDASI JIKA BUTTON
        from scraper import scraper
        data = {"tag": scraper.getheader(self.inputs[args])["tag"], "id": scraper.getheader(self.inputs[args])["id"],
             "class": scraper.getheader(self.inputs[args])["class"],
             "name": scraper.getheader(self.inputs[args])["name"], "value": "{button.click}",
             "innerHTML": scraper.getheader(self.inputs[args])["innerHTML"],
             "original_value": scraper.getheader(self.inputs[args])["value"],
             }
        self.list_of_input.append(data)
        self.parentWindow.set_input_table(data)

    def __init__(self, url, result, parent=None):
        super(InputResultTable, self).__init__(parent)
        self.parentWindow = parent
        self.url = url
        self.list_of_input = []

        self.setColumnCount(6)

        header = ("Type", "Id", "Name", "Value", "Action", "Inner")
        self.setHorizontalHeaderLabels(header)

        self.inputs = find_all_input(result) + find_all_button(result) + find_all_textarea(result)
        self.setRowCount(len(self.inputs))
        self.horizontalHeader().setSectionResizeMode(1)

        self.rowcount = 0
        for inp in self.inputs:
            header = getheader(inp)
            if header["innerHTML"] is not None and header["innerHTML"].lower() == "submit":
                itemtype = QTableWidgetItem(header["innerHTML"])
            else:
                itemtype = QTableWidgetItem(header["type"])
            itemid = QTableWidgetItem(header["id"])
            itemname = QTableWidgetItem(header["name"])
            iteminner = QTableWidgetItem(header["innerHTML"])

            itemtype.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemid.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemname.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)

            self.setItem(self.rowcount, 0, itemtype)
            self.setItem(self.rowcount, 1, itemid)
            self.setItem(self.rowcount, 2, itemname)
            self.setItem(self.rowcount, 3, QTableWidgetItem(header["value"]))
            self.setItem(self.rowcount, 4, iteminner)
            input_button = QPushButton("Click")
            input_button.clicked.connect(partial(self.on_click, self.rowcount))
            self.setCellWidget(self.rowcount, 4, input_button)

            self.rowcount += 1

        self.cellChanged.connect(self.cell_changed_reaction)
