from meta import meta


class SuperGlobal(metaclass=meta.Singleton):
    expected = {
        "url_after": None,
        "text_after": None,
        "element_after": None
    }
    title = ""
    timeout = 2



