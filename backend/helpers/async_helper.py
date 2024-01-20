import asyncio
import aiohttp
from appsettings import address


async def async_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{address}/{url}") as response:
            data = await response.json()
            return data


def create_task_request(task):
    return asyncio.create_task(task)


def run_action_async(task):
    return asyncio.create_task(async_request(task))
