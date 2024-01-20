import enum
from datetime import datetime

from abstract.test_runner import TestRunner


class ReportDetails:
    def __init__(self, name):
        self.name = self.__class__.__name__ + "_" + name
        self.error = self.Results.NONE.value
        self.elapsed_time = None
        self.start_time = None
        self.end_time = None
        self.format_date = '%Y-%m-%d %H:%M:%S'
        self.runner = TestRunner()

    class TypeOfTestContainers(enum.Enum):
        TEST = "Test"
        TEST_BUNDLE = "TestBundle"
        TEST_BUNDLE_COLLECTION = "TestBundleCollection"

    class Results(enum.Enum):
        NONE = "None"
        PASS = "Pass"
        FAIL = "Fail"
        PARTIAL_FAILURE = "Partial Failure"
        SCRIPT_ERROR = "Script"
        CONFIGURATION = "Configuration"

    def to_string(self):
        string = {
            'name': self.name,
            'error': self.error,
            'elapsed_time': self.elapsed_time,
            'start_time': self.start_time
        }
        return f"{string}"

    def start_timer(self):
        self.start_time = datetime.now().strftime(self.format_date)
        print(self.start_time, ": Running", self.name)

    def stop_timer(self):
        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        print(self.end_time, ": Finished", self.name, "in", self.elapsed_time, "minutes", "with error:", self.error)

        self.error = self.Results.PASS.value
