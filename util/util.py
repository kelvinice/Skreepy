import meta
import uuid


def uuid():
    return uuid.uuid4()


class Util(metaclass=meta.Singleton):

    def fake(self, type):
        pass


print(uuid())
