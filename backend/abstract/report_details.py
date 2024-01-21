import enum
from datetime import datetime

from abstract.test_runner import TestRunner


class ReportDetails:
    def __init__(self, name):
        self.name = self.__class__.__name__ + "_" + name
        self.type = str(self.__class__.__base__).replace("'>", "").split('.')[-1]
        self.result = self.Results.NONE.value
        self.elapsed_time = None
        self.start_time = None
        self.end_time = None
        self.format_date = '%Y-%m-%d %H:%M:%S'
        self.runner = TestRunner()

    class Results(enum.Enum):
        NONE = "None"
        PASS = "Pass"
        FAIL = "Fail"
        PARTIAL_FAILURE = "Partial Failure"
        SCRIPT_ERROR = "Script Error"
        CONFIGURATION_ERROR = "Configuration Error"

    def to_string(self):
        string = {
            'name': self.name,
            'result': self.result,
            'elapsed_time': self.elapsed_time,
            'start_time': self.start_time,
            'type': self.type
        }
        return f"{string}"

    def start_timer(self):
        self.start_time = datetime.now().strftime(self.format_date)
        print(self.start_time, ": Running", self.name)

    def stop_timer(self):
        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        print(self.end_time, ": Finished", self.name, "in", self.elapsed_time, "minutes", "with error:", self.result)

        self.result = self.Results.PASS.value
