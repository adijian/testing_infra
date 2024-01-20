from singleton_decorator import singleton


@singleton
class TestRunner:
    def __init__(self):
        self._running_test = []
        self._running_bundle = []
        self._running_bundle_collection = []

    @property
    def running_test(self):
        return self._running_test

    @running_test.setter
    def running_test(self, value):
        self._running_test = value

    @property
    def running_bundle(self):
        return self._running_bundle

    @running_bundle.setter
    def running_bundle(self, value):
        self._running_bundle = value

    @property
    def running_bundle_collection(self):
        return self._running_bundle_collection

    @running_bundle_collection.setter
    def running_bundle_collection(self, value):
        self._running_bundle_collection = value
