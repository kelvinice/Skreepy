from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import main
from scraper.resultter import Result_displayer
from scraper.scraper import getheader, find_all_input, find_all_button, find_all_textarea


class Automator():
    def execute(self):
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

        except TimeoutException:
            print("Timeout")
        finally:
            result = {
                "url_after" : scraper.browser.current_url,
                "text_found" : scraper.find_text(self.expected["text_after"]),
                "element_found" : scraper.find_element(self.expected["element_after"])
            }
            result_window = Result_displayer(url=self.url,expected=self.expected,result=result,parent=None)
            result_window.show()
            scraper.browser.close()

    def execute_rule(self):
        for inp in self.inputs:
            head = getheader(inp)
            for rule in self.rules:
                if('name' in rule and rule["name"] == head["name"]):
                    self.listofinputed.append(
                        {"tag": head["tag"],
                         "id": head["id"],
                         "class": head["class"],
                         "name": head["name"], "value": rule["value"]})
                elif('type' in rule and rule["type"] == head["type"]):
                    self.listofinputed.append(
                        {"tag": head["tag"],
                         "id": head["id"],
                         "class": head["class"],
                         "name": head["name"], "value": rule["value"]})


    def define_rule(self):
        self.rules.append({
            "name": "username",
            "value": "2001561335"
        })
        self.rules.append({
            "name": "password",
            "value": "13101998"
        })
        self.rules.append({
            "type":"submit",
            "value":"{button.click}"
        })

    def define_expected(self):
        self.expected["url_after"] = None
        self.expected["text_after"] = None
        self.expected["element_after"] = None

        self.expected["url_after"] = "https://industry.socs.binus.ac.id/learning-plan/"
        self.expected["text_after"] = "All approved"
        self.expected["element_after"] = "pushable"


    def __init__(self, url, result):
        super(Automator, self).__init__()
        self.rules = []
        self.expected = {}

        self.url = url
        self.listofinputed = []
        self.inputs = result
        self.inputs = find_all_input(result) + find_all_button(result) + find_all_textarea(result)
        self.rowCount = len(self.inputs)

        self.define_rule()
        self.define_expected()
        self.execute_rule()
        self.execute()



if __name__ == "__main__":
    main.main()