import meta
import uuid
from faker import Faker
from meta import meta


def get_uuid():
    return uuid.uuid4()


def get_today():
    from datetime import datetime
    return datetime.today().strftime('%d %b %Y')


class Util(metaclass=meta.Singleton):
    def fake(self, type):
        pass

    def get_expected(self):
        return self.expected
