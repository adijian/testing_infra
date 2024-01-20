import uuid
from abc import abstractmethod
from datetime import datetime

from abstract.results import Results


class Action:
    def __init__(self, action: str):
        self.action_name = action + "_" + uuid.uuid4().hex[:6]
        self.error = Results.NONE.value
        self.start_time = None
        self.end_time = None
        self.elapsed_time = None

    async def run(self):
        print("Running action", self.action_name)
        format_date = '%Y-%m-%d %H:%M:%S'
        self.start_time = datetime.now().strftime(format_date)

        await self.action_run()

        self.end_time = datetime.now().strftime(format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, format_date) - datetime.strptime(self.start_time, format_date)).total_seconds() / 60, 2)

        self.error = Results.PASS.value

        print("Finished action", self.action_name, "in", self.elapsed_time, "minutes with result", self.error)
        return f'{self.__dict__}'

    @abstractmethod
    async def action_run(self):
        pass
