import requests

from abstract.report_details import ReportDetails
from appsettings import address


class TestBundleCollection(ReportDetails):
    def __init__(self, name, collection: list[str]):
        super().__init__(
            name=name
        )
        self.collection = collection
        self.results = []

    def run(self):
        self.start_timer()
        self.runner.running_bundle_collection = self

        for collection in self.collection:
            response = requests.get(f"{address}/{collection}")
            self.results.append(response.json())

        self.stop_timer()
        self.runner.running_bundle_collection = []
        return {self.to_string(): self.results}

