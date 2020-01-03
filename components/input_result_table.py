from functools import partial

import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from scraper.resultter import Result_displayer
from scraper.scraper import find_all_input, find_all_button, find_all_textarea, getheader, find_all_form
from util.util import get_today, get_uuid


class InputResultTable(QTableWidget):
    def execute_all_click(self):
        print("executed")
        description = ""

        from scraper import scraper
        from util.superglobal import SuperGlobal

        scraper.browser = scraper.dive_plus(self.url, self.list_of_input)

        wait = WebDriverWait(scraper.browser, SuperGlobal.timeout)
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
                "text_found": scraper.find_text(SuperGlobal.expected["text_after"]),
                "element_found": scraper.find_element(SuperGlobal.expected["element_after"])
            }
            data = {
                "result": result,
                "expected": SuperGlobal.expected,
                "id": str(get_uuid()),
                "date": get_today(),
                "title": "Skreepy",
                "description": description
            }
            if SuperGlobal.close_browser_after_test:
                scraper.browser.close()
            from ui.report_window import ReportWindow
            o = ReportWindow(1000, 680, data=data, parent=self)
            o.setVisible(True)

    def cell_changed_reaction(self, row, col):
        # Value changed
        if col == 3:
            print("Value Change To : " + str(self.item(row, col).text()))
            from scraper import scraper
            text = str(self.item(row, col).text())
            self.list_of_input.append(
                {"tag": scraper.getheader(self.inputs[row])["tag"], "id": scraper.getheader(self.inputs[row])["id"],
                 "class": scraper.getheader(self.inputs[row])["class"],
                 "name": scraper.getheader(self.inputs[row])["name"], "value": text})

    def on_click(self, args=0):
        # TODO VALIDASI JIKA BUTTON
        from scraper import scraper
        self.list_of_input.append(
            {"tag": scraper.getheader(self.inputs[args])["tag"], "id": scraper.getheader(self.inputs[args])["id"],
             "class": scraper.getheader(self.inputs[args])["class"],
             "name": scraper.getheader(self.inputs[args])["name"], "value": "{button.click}"})

    def __init__(self, url, result, parent=None):
        super(InputResultTable, self).__init__(parent)

        self.url = url
        self.list_of_input = []

        self.setColumnCount(6)

        header = ("Type", "Id", "Name", "Value", "Action", "Inner")
        self.setHorizontalHeaderLabels(header)

        self.inputs = find_all_input(result) + find_all_button(result) + find_all_textarea(result)
        self.setRowCount(len(self.inputs))

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
