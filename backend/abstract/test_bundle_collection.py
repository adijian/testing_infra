import requests

from appsettings import address


class TestBundleCollection:
    def __init__(self, collection: list[str]):
        self.collection = collection
        self.results = []

    def run(self):
        for collection in self.collection:
            response = requests.get(f"{address}/{collection}")
            self.results.append({collection: response.json()})
        return {"Collection Results": self.results}
