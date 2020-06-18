from tests.fixtures.test_client import TestClient


def add_test_client():

    def class_wrapper(original_class):
        original_init = original_class.__init__

        def __init__(self, *args, **kws):
            self.test_client = TestClient.create()
            original_init(self, *args, **kws)

        original_class.__init__ = __init__
        return original_class

    return class_wrapper
