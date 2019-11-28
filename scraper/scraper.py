import os

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://thin-skinned-passes.000webhostapp.com/login.php'
url2 = 'https://thin-skinned-passes.000webhostapp.com'

url = 'http://industry.socs.binus.ac.id/learning-plan/auth/login'
url2 = 'http://industry.socs.binus.ac.id/learning-plan/'
session = requests.Session()
browser = None


def scrape(url):
    req = session.get(url)
    if req.status_code != requests.codes.ok:
        print(url, " Unreachable")
        return
    return req.content


def findallform(htmldata):
    soup = BeautifulSoup(htmldata, features='html.parser')
    forms = soup.find_all('form')
    return forms


def findallinput(htmldata):
    inputs = htmldata.find_all('input')
    return inputs


def findallbutton(htmldata):
    inputs = htmldata.find_all('button')
    return inputs


def findalltextarea(htmldata):
    inputs = htmldata.find_all('textarea')
    return inputs


def innerHTML(element):
    """Returns the inner HTML of an element as a UTF-8 encoded bytestring"""
    return element.encode_contents()


def getheader(htmldata):
    header = {}
    header["id"] = "None"
    header["class"] = "None"

    header["method"] = htmldata.get("method")
    header["action"] = htmldata.get("action")
    header["id"] = htmldata.get("id")
    header["class"] = htmldata.get("class")
    header["type"] = htmldata.get("type")
    header["value"] = htmldata.get("value")
    header["name"] = htmldata.get("name")
    header["innerHTML"] = htmldata.text
    header["tag"] = htmldata.name
    return header


listofinputed = []


def getInputed(inputs, choose):
    listofinputed.append({"id": getheader(inputs[choose])["id"], "class": getheader(inputs[choose])["class"],
                          "name": getheader(inputs[choose])["name"], "value": value})
    inputs[choose]['value'] = value


def get_browser():
    return browser


def dive(url, listofinputed):
    browsers = get_browser()
    if browsers == None:
        browsers = webdriver.Firefox()
    browsers.get(url)
    for inputed in listofinputed:

        if inputed["id"] != None:
            input_inputed = browsers.find_element_by_id(inputed["id"])
        else:
            # classname = ".".join(getheader(inputed)["class"])
            input_inputed = browsers.find_element_by_name(inputed["name"])
        input_inputed.send_keys(inputed["value"])
    return browsers


def find_text(text):
    browsers = get_browser()
    try:
        res = browsers.find_elements_by_xpath("//*[contains(text(), '" + text + "')]")
        if len(res) == 0: return False
        return True
    except:
        return False


def find_element(element):
    browsers = get_browser()
    try:
        res_id = browsers.find_elements_by_xpath("//*[@id='" + element + "']")
        res_class = browsers.find_elements_by_xpath("//*[contains(@class,'" + element + "')]")
        print(res_id)
        print(res_class)
        if len(res_id) == 0 and len(res_class) == 0: return False
        return True
    except:
        return False


def dive_plus(url, listofinputed):
    browsers = get_browser()
    if browsers == None:
        browsers = webdriver.Firefox()
    browsers.get(url)

    for inputed in listofinputed:
        if inputed["value"] == "{button.click}":
            print(inputed)
            if inputed["id"] != None:
                print("using id")
                submit = browsers.find_element_by_id(inputed["id"])
            elif inputed["class"] != None:
                classname = ".".join(inputed["class"])
                print("using css", classname)
                if inputed["tag"] == "input":
                    print("pake input")
                    submit = browsers.find_element_by_css_selector('input.' + classname)
                else:
                    print("pake button")
                    submit = browsers.find_element_by_css_selector('button.' + classname)
                    print("bbb")
            submit.click()

        elif inputed["id"] != None:
            input_inputed = browsers.find_element_by_id(inputed["id"])
            input_inputed.send_keys(inputed["value"])
        else:
            input_inputed = browsers.find_element_by_name(inputed["name"])
            input_inputed.send_keys(inputed["value"])

    return browsers


def processform(formdata):
    choose = 0

    while choose != -1:
        # os.system("cls")
        inputs = findallinput(formdata)
        print("Input List : \n")
        for i in range(0, len(inputs)):
            header = getheader(inputs[i])
            print(i, " type : ", header["type"], " id : ", header["id"], " name : ", header["name"], " value : ",
                  header["value"])
        choose = int(input("Choose [-1 for exit] : "))

        if choose >= 0 and choose < len(inputs):
            if inputs[choose]["type"] == "submit":
                browser = webdriver.Firefox()
                browser.get(url)

                for inputed in listofinputed:

                    if inputed["id"] != None:
                        input_inputed = browser.find_element_by_id(inputed["id"])
                    else:
                        # classname = ".".join(getheader(inputed)["class"])
                        input_inputed = browser.find_element_by_name(inputed["name"])
                    input_inputed.send_keys(inputed["value"])

                # print(classname)
                if getheader(inputs[choose])["id"] != None:
                    # print("using id")
                    submit = browser.find_element_by_id(inputs[choose]["id"])
                else:
                    classname = ".".join(getheader(inputs[choose])["class"])
                    # print("using css",classname)
                    submit = browser.find_element_by_css_selector('input.' + classname)
                submit.click()
                wait = WebDriverWait(browser, 5)
                try:
                    page_loaded = wait.until_not(
                        lambda browser: browser.current_url == url
                    )
                    print("Page is ready!")
                    cookies = browser.get_cookies()

                    for cookie in cookies:
                        print(cookie['name'], " : ", cookie['value'])
                        session.cookies.set(cookie['name'], cookie['value'])
                    loginResult = scrape(url2)
                    soup = BeautifulSoup(loginResult, features='html.parser')

                    # print(soup.find_all('div',{"id": "core-content"}))
                    print(soup.find_all('div', {"class": "ui success message"}))
                except TimeoutException:
                    print("Timeout")



            else:
                value = input("Change value: ")
                listofinputed.append(
                    {"id": getheader(inputs[choose])["id"], "class": getheader(inputs[choose])["class"],
                     "name": getheader(inputs[choose])["name"], "value": value})
                inputs[choose]['value'] = value


def set_cookies(browser, cookies):
    cookies = browser.get_cookies()

    for cookie in cookies:
        print(cookie['name'], " : ", cookie['value'])
        session.cookies.set(cookie['name'], cookie['value'])
    return cookies


def main():
    choose = 0

    loginResult = scrape(url)

    forms = findallform(loginResult)

    while choose != -1:
        os.system("cls")
        print("Form List : \n")
        for i in range(0, len(forms)):
            header = getheader(forms[i])
            print(i, " Method : ", header["method"], " Action : ", header["action"])
        print("")
        choose = int(input("Choose [-1 for exit] : "))
        if choose >= 0 and choose < len(forms):
            processform(forms[choose])

    # print(loginResult)


if __name__ == "__main__":
    # dic = {"a":"b"}
    # if dic["c"]:
    #     print("yes")
    # input("....")
    main()

# baru
