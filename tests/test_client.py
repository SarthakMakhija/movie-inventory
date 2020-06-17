from tests.fixtures.test_client import TestClient


def add_test_client():

    def class_wrapper(original_class):
        orig_init = original_class.__init__

        # Make copy of original __init__, so we can call it without recursion

        def __init__(self, *args, **kws):
            self.test_client = TestClient.create()
            orig_init(self, *args, **kws)  # Call the original __init__

        original_class.__init__ = __init__  # Set the class' __init__ to the new one
        return original_class

    return class_wrapper
