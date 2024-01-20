from datetime import datetime

import requests

from abstract.results import Results
from appsettings import address


class TestBundle:
    def __init__(self, name, tests: list[str]):
        self.test_bundle_name = name + datetime.now().strftime("_%d-%m-%Y%H:%M:%S.%f")[:-3]
        self.tests = tests
        self.error = Results.NONE.value
        self.results = []
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    def run(self):
        format_date = '%Y-%m-%d %H:%M:%S'
        self.start_time = datetime.now().strftime(format_date)

        for test in self.tests:
            response = requests.get(f"{address}/{test}")
            self.results.append(response.json())

        self.end_time = datetime.now().strftime(format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, format_date) - datetime.strptime(self.start_time, format_date)).total_seconds() / 60, 2)

        self.error = Results.PASS.value

        return {self.to_string(): self.results}

    def to_string(self):
        string = {
            'test_bundle_name': self.test_bundle_name,
            'error': self.error,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'elapsed_time': self.elapsed_time
        }
        return f"{string}"
