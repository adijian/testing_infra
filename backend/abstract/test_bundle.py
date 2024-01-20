from datetime import datetime

import requests

from abstract.report_details import ReportDetails
from appsettings import address


class TestBundle(ReportDetails):
    def __init__(self, name, tests: list[str]):
        super().__init__(
            name=name
        )
        self.tests = tests
        self.results = []

    def run(self):
        self.start_time = datetime.now().strftime(self.format_date)

        for test in self.tests:
            response = requests.get(f"{address}/{test}")
            self.results.append(response.json())

        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        self.error = self.Results.PASS.value

        return {self.to_string(): self.results}

    # def to_string(self):
    #     string = {
    #         'test_bundle_name': self.test_bundle_name,
    #         'error': self.error,
    #         'start_time': self.start_time,
    #         'end_time': self.end_time,
    #         'elapsed_time': self.elapsed_time
    #     }
    #     return f"{string}"
