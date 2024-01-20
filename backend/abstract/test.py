import time
from abc import abstractmethod
from datetime import datetime

from helpers.async_helper import *


class Test:
    def __init__(self, name):
        self.name = name + datetime.now().strftime("_%d-%m-%Y%H:%M:%S.%f")[:-3]
        self.results = []
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None

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

        self.start_time = time.time()

        run_test = await self.test_run()

        self.end_time = time.time()
        self.elapsed_time = round((self.end_time - self.start_time) / 60, 2)

        print("Finished test", self.name, "in", self.elapsed_time, "minutes")

        return run_test

    @abstractmethod
    async def test_run(self):
        pass
