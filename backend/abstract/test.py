from abc import abstractmethod

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
        :param path: the action to start running
        """
        self.results.append(await create_task_request(async_request(path)))

    async def run_multiple_actions_sync(self, paths: list):
        """
        Runs multiple actions and waits for their results
        :param paths:
        """
        tasks = [async_request(path) for path in paths]
        results = await asyncio.gather(*tasks)
        for i in range(len(results)):
            self.results.append(paths[i] + " " + results[i])

    async def run(self):
        self.start_timer()
        self.runner.running_test = []

        run_test = await self.test_run()

        self.stop_timer()
        self.runner.running_test = []
        return {self.to_string(): run_test}

    @abstractmethod
    async def test_run(self):
        pass

