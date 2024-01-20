from singleton_decorator import singleton


@singleton
class TestRunner:
    def __init__(self):
        self.is_running = False

    @property
    def is_running(self):
        return self.is_running

    @is_running.setter
    def is_running(self, value):
        self._is_running = value
