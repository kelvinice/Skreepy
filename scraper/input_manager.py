from functools import partial

import PyQt5.QtCore
from PyQt5.QtWidgets import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import main
from scraper.resultter import Result_displayer


class input_manager(QMainWindow):
    def cellChanged(self,row, col):

        #Value changed
        if col==3:
            print("Value Change To : "+str(self.tblForm.item(row,col).text()))
            import scraper
            text = str(self.tblForm.item(row,col).text())
            self.listofinputed.append(
                {"tag": scraper.getheader(self.inputs[row])["tag"], "id": scraper.getheader(self.inputs[row])["id"], "class": scraper.getheader(self.inputs[row])["class"],
                 "name": scraper.getheader(self.inputs[row])["name"], "value": text})


    def on_click(self,args=0):
        # TODO VALIDASI JIKA BUTTON
        import scraper
        self.listofinputed.append(
            {"tag": scraper.getheader(self.inputs[args])["tag"],"id": scraper.getheader(self.inputs[args])["id"], "class": scraper.getheader(self.inputs[args])["class"],
             "name": scraper.getheader(self.inputs[args])["name"], "value": "{button.click}"})
        # print(self.listofinputed)
        # if(str(self.tblForm.item(args,0).text()).lower()=="submit"):
        #     import scraper
        #     scraper.browser = scraper.dive(self.url, self.listofinputed)

        # else:
        #     pass

    def executeAllClick(self):
        print("executed")

        if self.exUrlLbl.text() != "" :
            self.expected["url_after"] = self.exUrlLbl.text()
        if self.exTextLbl.text() != "":
            self.expected["text_after"] = self.exTextLbl.text()
        if self.exElementLbl.text() != "":
            self.expected["element_after"] = self.exElementLbl.text()

        print(self.expected)

        import scraper
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
            result = {
                "url_after": scraper.browser.current_url,
                "text_found": scraper.find_text(self.expected["text_after"]),
                "element_found": scraper.find_element(self.expected["element_after"])
            }
            result_window = Result_displayer(url=self.url, expected=self.expected, result=result, parent=None)
            result_window.show()
            # scraper.browser.close()


    def save_click(self):
        import pickle
        with open('saved.pkl', 'wb') as f:
            pickle.dump(self.listofinputed, f)

    def setValueByInput(self,inputed):
        i = 0
        for input in self.inputs:
            import scraper
            head = scraper.getheader(input)
            if head["id"]==inputed["id"] and head["class"] == inputed["class"] and head["tag"] == inputed["tag"] and head["name"] == inputed["name"]:
                # print(head)
                self.tblForm.item(i, 3).setText(inputed["value"])
            i+=1
            # self.tblForm.item(row, col).text()
            # print(i["value"])

    def load_click(self):
        import pickle
        with open('saved.pkl', 'rb') as f:
            self.listofinputed = pickle.load(f)
        for inputed in self.listofinputed:
            if inputed["value"] != "{button.click}":
                self.setValueByInput(inputed)

    def __init__(self, url,result, parent=None):
        super(input_manager, self).__init__(parent)
        self.url = url
        self.listofinputed= []
        self.inputs = result
        self.tblForm = QTableWidget()
        self.expected = {}
        self.expected["url_after"] = None
        self.expected["text_after"] = None
        self.expected["element_after"] = None

        from scraper import getheader, findallinput,findallbutton,findalltextarea

        self.inputs = findallinput(result)+findallbutton(result)+findalltextarea(result)

        self.tblForm.setRowCount(len(self.inputs))

        self.tblForm.setColumnCount(6)

        header = ("Type", "Id", "Name", "Value", "Action","Inner")
        self.tblForm.setHorizontalHeaderLabels(header)

        self.rowcount = 0
        for inp in self.inputs:
            header = getheader(inp)
            if header["innerHTML"]!= None and header["innerHTML"].lower()=="submit":
                itemtype = QTableWidgetItem(header["innerHTML"])
            else:
                itemtype = QTableWidgetItem(header["type"])
            itemid = QTableWidgetItem(header["id"])
            itemname = QTableWidgetItem(header["name"])
            iteminner = QTableWidgetItem(header["innerHTML"])

            itemtype.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemid.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)
            itemname.setFlags(itemtype.flags() & ~PyQt5.QtCore.Qt.ItemIsEditable & ~PyQt5.QtCore.Qt.TextEditable)

            self.tblForm.setItem(self.rowcount, 0, itemtype)
            self.tblForm.setItem(self.rowcount, 1, itemid)
            self.tblForm.setItem(self.rowcount, 2, itemname)
            self.tblForm.setItem(self.rowcount, 3, QTableWidgetItem(header["value"]))
            self.tblForm.setItem(self.rowcount, 4, iteminner)
            input_button = QPushButton("Click")
            input_button.clicked.connect(partial(self.on_click, self.rowcount))
            self.tblForm.setCellWidget(self.rowcount, 4, input_button)

            self.rowcount += 1

        self.tblForm.cellChanged.connect(self.cellChanged)
        layout = QVBoxLayout()
        self.browser_shower = QTextEdit(str(result))
        self.execute_button = QPushButton("Execute")
        self.save_button = QPushButton("Save")
        self.load_button = QPushButton("Load")

        self.execute_button.clicked.connect(self.executeAllClick)
        self.save_button.clicked.connect(self.save_click)
        self.load_button.clicked.connect(self.load_click)

        layout.addWidget(self.browser_shower)
        layout.addWidget(self.tblForm)
        layout.addWidget(self.execute_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.load_button)

        self.exUrlLbl = QLineEdit()
        gridAction1 = QGridLayout()
        gridAction1.setColumnStretch(1, 2)
        gridAction1.addWidget(QLabel("Url Expected"))
        gridAction1.addWidget(self.exUrlLbl)
        leftright1 = QWidget()
        leftright1.setLayout(gridAction1)
        layout.addWidget(leftright1)


        self.exTextLbl = QLineEdit()
        gridAction2 = QGridLayout()
        gridAction2.setColumnStretch(1, 2)
        gridAction2.addWidget(QLabel("Text Expected"))
        gridAction2.addWidget(self.exTextLbl)
        leftright2 = QWidget()
        leftright2.setLayout(gridAction2)
        layout.addWidget(leftright2)

        self.exElementLbl = QLineEdit()
        gridAction3 = QGridLayout()
        gridAction3.setColumnStretch(1, 2)
        gridAction3.addWidget(QLabel("Element Expected"))
        gridAction3.addWidget(self.exElementLbl)
        leftright3 = QWidget()
        leftright3.setLayout(gridAction3)
        layout.addWidget(leftright3)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)
        self.resize(600, 500)
        self.setWindowTitle("Input Manager")
        self.statusBar().showMessage("Active")

if __name__=="__main__":
    main.main()