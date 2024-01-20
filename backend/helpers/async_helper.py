import asyncio
import aiohttp
from appsettings import address


async def async_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{address}/{url}") as response:
            data = await response.json()
            return data


def create_task(task):
    return asyncio.create_task(task)
