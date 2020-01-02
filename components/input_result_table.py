from functools import partial

import PyQt5
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QPushButton
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from scraper.resultter import Result_displayer
from scraper.scraper import find_all_input, find_all_button, find_all_textarea, getheader, find_all_form


class InputResultTable(QTableWidget):
    def executeAllClick(self):
        print("executed")
        from ui.report_window import ReportWindow
        w = ReportWindow(800, 1000, "Skreepy")

        # TODO
        # if self.exUrlLbl.text() != "":
        #     self.expected["url_after"] = self.exUrlLbl.text()
        # if self.exTextLbl.text() != "":
        #     self.expected["text_after"] = self.exTextLbl.text()
        # if self.exElementLbl.text() != "":
        #     self.expected["element_after"] = self.exElementLbl.text()

        # print(self.expected)

        from scraper import scraper
        scraper.browser = scraper.dive_plus(self.url, self.listofinputed)

        wait = WebDriverWait(scraper.browser, 5)
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
        finally:
            from util.super_global import super_global
            print(super_global.expected["text_after"])
            result = {
                "url_after": scraper.browser.current_url,
                "text_found": scraper.find_text(super_global.expected["text_after"]),
                "element_found": scraper.find_element(super_global.expected["element_after"])
            }

            # OLD
            # result_window = Result_displayer(url=self.url, expected=super_global.expected, result=result, parent=None)
            # result_window.show()

            # NEW

            w.show()
            print("show report")

    def cellChangedReaction(self, row, col):
        # Value changed
        if col == 3:
            print("Value Change To : " + str(self.item(row, col).text()))
            from scraper import scraper
            text = str(self.item(row, col).text())
            self.listofinputed.append(
                {"tag": scraper.getheader(self.inputs[row])["tag"], "id": scraper.getheader(self.inputs[row])["id"],
                 "class": scraper.getheader(self.inputs[row])["class"],
                 "name": scraper.getheader(self.inputs[row])["name"], "value": text})

    def on_click(self, args=0):
        # TODO VALIDASI JIKA BUTTON
        from scraper import scraper
        self.listofinputed.append(
            {"tag": scraper.getheader(self.inputs[args])["tag"], "id": scraper.getheader(self.inputs[args])["id"],
             "class": scraper.getheader(self.inputs[args])["class"],
             "name": scraper.getheader(self.inputs[args])["name"], "value": "{button.click}"})

    def __init__(self, url, result, parent=None):
        super(InputResultTable, self).__init__(parent)

        self.url = url
        self.listofinputed = []

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

        self.cellChanged.connect(self.cellChangedReaction)
