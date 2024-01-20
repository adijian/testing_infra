import time
from abc import abstractmethod

from helpers.async_helper import *


class Test:
    def __init__(self):
        self.results = []
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None

    async def validate_task_completion(self, path, task):
        self.results.append({path: await task})

    async def run_action_sync(self, path):
        self.results.append({path: await create_task_request(async_request(path))})

    async def run_multiple_actions_sync(self, paths: list):
        tasks = [async_request(path) for path in paths]
        results = await asyncio.gather(*tasks)
        for i in range(len(results)):
            self.results.append(paths[i] + " " + results[i])

    async def run(self):
        return await self.test_run()

    @abstractmethod
    async def test_run(self):
        pass
