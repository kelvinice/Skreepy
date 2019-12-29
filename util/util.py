import meta
import uuid
from faker import Faker
from meta import meta


def uuid():
    return uuid.uuid4()


class Util(metaclass=meta.Singleton):


    def fake(self, type):
        pass

    def get_expected(self):
        return self.expected
