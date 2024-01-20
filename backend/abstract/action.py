from abc import abstractmethod

from abstract.report_details import ReportDetails


class Action(ReportDetails):
    def __init__(self, name):
        super().__init__(name)

    async def run(self):
        self.start_timer()

        await self.action_run()

        self.stop_timer()
        return self.to_string()

    @abstractmethod
    async def action_run(self):
        pass
