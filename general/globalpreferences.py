from meta import singleton


class GlobalPreferences(metaclass=singleton.Singleton):
    setting = {
        "expected": {
            "url_after": "",
            "text_after": "",
            "element_after": ""
        },
        "title": "",
        "timeout": 1,
        "close_browser_after_test": False,
        "tester": "Chen"
    }








