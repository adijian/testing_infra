from datetime import datetime

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
        format_date = '%Y-%m-%d %H:%M:%S'
        self.start_time = datetime.now().strftime(self.format_date)

        for collection in self.collection:
            response = requests.get(f"{address}/{collection}")
            self.results.append(response.json())

        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        self.error = self.Results.PASS.value

        return {self.to_string(): self.results}

    # def to_string(self):
    #     string = {
    #         'name': self.name,
    #         'error': self.error,
    #         'start_time': self.start_time,
    #         'end_time': self.end_time,
    #         'elapsed_time': self.elapsed_time
    #     }
    #     return f"{string}"
