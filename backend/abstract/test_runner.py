from singleton_decorator import singleton


@singleton
class TestRunner:
    def __init__(self):
        self.running_tests = []
        self.running_bundle = []
        self.running_bundle_collection = []