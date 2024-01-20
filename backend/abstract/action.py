import asyncio

from abstract.results import Results


class Action:
    def __init__(self):
        self.name = 'action'
        self.error = Results.NONE.value

    async def run(self):
        print("Running action", self.name)
        await asyncio.sleep(3)
        self.error = Results.PASS.value
        return f'{self.__dict__}'
