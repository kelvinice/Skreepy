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
