# import time
#
# from abstract.test import Test
#
#
# class TestOne(Test):
#     async def test_run(self):
#         print("Running test one")
#         self.start_time = time.time()
#         # await self.run_action("action")
#         await self.run_multiple_actions(["action", "action"])
#         self.end_time = time.time()
#         self.elapsed_time = self.start_time - self.end_time
#         return self.results
