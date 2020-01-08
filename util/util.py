import json
import os

import meta
import uuid
from faker import Faker
from meta import meta
from util.superglobal import SuperGlobal


def get_uuid():
    return uuid.uuid4()


def get_today():
    from datetime import datetime
    return datetime.today().strftime('%d-%b-%Y %H:%M:%S')


def read_from_file(path):
    cwd = os.getcwd()
    file = open(cwd + path, "r")
    content = file.read()
    file.close()
    return content


def write_to_file(path, content):
    cwd = os.getcwd()
    file = open(cwd + path, "w+")
    file.write(content)
    file.close()


def export_to_html(data):
    template = read_from_file("\\template\\template.html")
    css = read_from_file("\\template\\style.css")

    if data["overall_result"]:
        overall_result = '<div class="success">PASSED</div>'
    else:
        overall_result = '<div class="failed">FAILED</div>'

    expected = data["expected"]
    result = data["result"]

    res = template.format(
        id=data["id"],
        title=data["title"],
        overall_result=overall_result,
        css=css,
        date=data["date"],
        description=data["description"],
        expected_url=expected["url_after"],
        expected_element=expected["element_after"],
        expected_text=expected["text_after"],
        result_url=result["url_after"],
        result_element=result["element_found"],
        result_text=result["text_found"],
        tester=data["tester"]
    )

    new = 2
    write_to_file("\\output\\output.html", res)

    import webbrowser
    cwd = os.getcwd()
    url = cwd + "\\output\\output.html"
    webbrowser.open(url, new=new)


def load_setting():
    cwd = os.getcwd()
    file = open(cwd + "\\config\\setting.json", "r")

    setting = json.load(file)
    SuperGlobal.setting = setting
    file.close()


def save_setting():
    cwd = os.getcwd()
    file = open(cwd + "\\config\\setting.json", "w+")

    data = SuperGlobal.setting
    json.dump(data, file)
    file.close()


def to_bool(i):
    if int(i) == 0:
        return False
    return True


class Util(metaclass=meta.Singleton):
    def fake(self, type):
        pass
