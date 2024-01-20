from abc import abstractmethod
from datetime import datetime

from abstract.report_details import ReportDetails
from helpers.async_helper import *


class Test(ReportDetails):
    def __init__(self, name):
        super().__init__(
            name=name
        )
        self.results = []

    async def validate_action_completion(self, action):
        """
        Starts an action. The action needs to be waited for in order to receive the result.
        :param action: the action to start running
        """
        self.results.append(await action)

    async def run_action_sync(self, path):
        """
        Starts and waits for the result of an action
        :param path:
        """
        self.results.append(await create_task_request(async_request(path)))

    async def run_multiple_actions_sync(self, paths: list):
        """
        Runs multiple actions and waits for their results
        :param paths:
        :return:
        """
        tasks = [async_request(path) for path in paths]
        results = await asyncio.gather(*tasks)
        for i in range(len(results)):
            self.results.append(paths[i] + " " + results[i])

    async def run(self):
        print("Running test", self.name)
        self.start_time = datetime.now().strftime(self.format_date)

        run_test = await self.test_run()

        self.end_time = datetime.now().strftime(self.format_date)
        self.elapsed_time = round((datetime.strptime(self.end_time, self.format_date) - datetime.strptime(self.start_time, self.format_date)).total_seconds() / 60, 2)

        print("Finished test", self.name, "in", self.elapsed_time, "minutes")

        self.error = self.Results.PASS.value
        return {self.to_string(): run_test}

    @abstractmethod
    async def test_run(self):
        pass

    # def to_string(self):
    #     string = {
    #         'test_name': self.test_name,
    #         'error': self.error,
    #         'start_time': self.start_time,
    #         'end_time': self.end_time,
    #         'elapsed_time': self.elapsed_time
    #     }
    #     return f"{string}"
