import asyncio
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from abstract.action import Action
from abstract.test import Test
from abstract.test_bundle import TestBundle
from abstract.test_bundle_collection import TestBundleCollection
from abstract.test_runner import TestRunner
from appsettings import port
# from tests.test_one import TestOne

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

""""
# frontend requests number of test bundles to display in dropdown
# user picks a test bundle
# backend separates calls to a list and returns a list of actions
# * do I iterate over list from backend?
# * how will the user contact the frontend? -- use api call to contact front to return current test's logs?
# * are test results HTTP results?-


# how do I let the user store api responses as variables
"""


@app.get("/")
def get_all_urls(request: Request):
    url_list = [route.path for route in request.app.routes]
    return url_list


@app.get("/action")
async def action():
    return await Action().run()


@app.get("/test")
async def test():
    import time
    from abstract.test import Test

    class TestOne(Test):
        async def test_run(self):
            print("Running test one")
            self.start_time = time.time()
            # await self.run_action("action")
            await self.run_multiple_actions(["action", "action"])
            self.end_time = time.time()
            self.elapsed_time = self.start_time - self.end_time
            return self.results

    return await TestOne().run()


@app.get("/test_bundle")
def test_bundle():
    return TestBundle(tests=[
        "test",
        "test"
    ]).run()


@app.get("/test_bundle_collection")
def test_bundle_collection():
    return TestBundleCollection(collection=[
        "test_bundle",
        "test_bundle"
    ]).run()


if __name__ == "__main__":
    TestRunner()
    uvicorn.run(app, host="0.0.0.0", port=port)
