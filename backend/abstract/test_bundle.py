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
        self.start_timer()
        self.runner.running_bundle = self

        for test in self.tests:
            response = requests.get(f"{address}/{test}")
            self.results.append(response.json())

        self.stop_timer()
        self.runner.running_bundle = []
        return {self.to_string(): self.results}
