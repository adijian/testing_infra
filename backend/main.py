import asyncio
import time
from asyncio import create_task
from typing import List

import requests
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket, WebSocketDisconnect

from abstract.action import Action
from abstract.test import Test
from abstract.test_bundle import TestBundle
from abstract.test_bundle_collection import TestBundleCollection
from abstract.test_runner import TestRunner
from appsettings import port
from helpers.async_helper import create_task_request, async_request, run_action_async

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
# * how will the user contact the frontend? -- use api call to contact front to return current test's logs?
"""


@app.get("/")
def get_all_urls(request: Request):
    url_list = [route.path for route in request.app.routes]
    return url_list


@app.get("/action")
async def action():
    class ActionOne(Action):
        async def action_run(self):
            return await asyncio.sleep(3)

    return await ActionOne('action').run()


@app.get("/test")
async def test():
    class TestOne(Test):
        async def test_run(self):
            # await self.run_action_sync("action")
            #
            # action_instance = run_action_async('action')
            # # Do other stuff
            # await self.validate_action_completion(action_instance)
            #

            list_of_instances = []
            for i in range(2):
                list_of_instances.append(run_action_async('action'))
            # Do other stuff

            # await self.run_action_sync("action")

            for i in range(len(list_of_instances)):
                await self.validate_action_completion(list_of_instances[i])
            return self.results

    return await TestOne('test').run()


@app.get("/test_bundle")
def test_bundle():
    return TestBundle(name="test_bundle",
                      tests=[
                          "test",
                          "test"
                      ]).run()


@app.get("/test_bundle_collection")
def test_bundle_collection():
    return TestBundleCollection(name="test_collection",
                                collection=[
                                    "test_bundle",
                                    "test_bundle"
                                ]).run()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_message(f"Message text was: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@app.post("/message")
async def send_message_to_ws(message: str):
    if not manager.active_connections:
        raise HTTPException(status_code=404, detail="No active websocket connections")
    await manager.send_message(message)


if __name__ == "__main__":
    TestRunner()
    uvicorn.run(app, host="0.0.0.0", port=port)
