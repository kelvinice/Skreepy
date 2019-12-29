from meta import meta


class super_global(metaclass=meta.Singleton):
    expected = {}

    def __init__(self):
        self.expected["url_after"] = None
        self.expected["text_after"] = None
        self.expected["element_after"] = None
