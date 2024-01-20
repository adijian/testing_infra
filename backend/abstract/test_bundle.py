import requests

from appsettings import address


class TestBundle:
    def __init__(self, tests: list[str]):
        self.tests = tests
        self.results = []

    def run(self):
        for test in self.tests:
            response = requests.get(f"{address}/{test}")
            self.results.append({test: response.json()})
        return self.results
