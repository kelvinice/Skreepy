import meta
import uuid
from faker import Faker


def uuid():
    return uuid.uuid4()


class Util(metaclass=meta.Singleton):

    def fake(self, type):
        pass
