import uuid
from abc import abstractmethod
from datetime import datetime

from abstract.report_details import ReportDetails


class Action(ReportDetails):
    def __init__(self, name):
        super().__init__(name)
        # self.action_name = action + "_" + uuid.uuid4().hex[:6]

    async def run(self):
        print("Running action", self.name)
        self.start_time = datetime.now().strftime(self.format_date)

        await self.action_run()

        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        self.error = self.Results.PASS.value

        print("Finished action", self.name, "in", self.elapsed_time, "minutes with result", self.error)
        return self.to_string()

    @abstractmethod
    async def action_run(self):
        pass
