import time
import uuid
from abc import abstractmethod
from abstract.results import Results


class Action:
    def __init__(self, action: str):
        id_num = uuid.uuid4().hex[:6]
        self.action_name = action + "_" + id_num
        self.id = id_num
        self.error = Results.NONE.value
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None

    async def run(self):
        print("Running action", self.action_name)
        self.start_time = time.time()

        await self.action_run()

        self.end_time = time.time()
        self.elapsed_time = round((self.end_time - self.start_time) / 60, 2)

        self.error = Results.PASS.value

        print("Finished action", self.action_name, "in", self.elapsed_time, "minutes with result", self.error)
        return f'{self.__dict__}'

    @abstractmethod
    async def action_run(self):
        pass
