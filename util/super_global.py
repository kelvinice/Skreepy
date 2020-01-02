from meta import meta


class super_global(metaclass=meta.Singleton):
    expected = {
        "url_after": None,
        "text_after": None,
        "element_after": None
    }

