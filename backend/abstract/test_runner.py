import time
from singleton_decorator import singleton


@singleton
class TestRunner:
    def __init__(self):
        self.results = []
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None
        self.is_running = False

    @property
    def is_running(self):
        return self.is_running

    @is_running.setter
    def is_running(self, value):
        self._is_running = value
