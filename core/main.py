# modified fetch function with semaphore
import random
import asyncio
from abc import ABC, abstractmethod

from aiohttp import ClientSession
from datetime import datetime

requests = 0
clients_num = 100
url = ''
start_time = datetime.now()


class Attacker(ABC):
    @abstractmethod
    def run(self):
        ...


async def make_request():
    async with ClientSession() as session:
        global requests
        print(f'Requests: {requests}')
        requests += 1
        response = await session.get(url)
        delay = response.headers.get("DELAY")
        date = response.headers.get("DATE")
        print(f"{date}:{response.url} with delay {delay}. Responce status: {response.status}")
        await print_rate()


async def start_clients():
    while True:
        await asyncio.sleep(0.005)
        asyncio.create_task(make_request())


async def print_rate():
    current_time = datetime.now()
    delta = current_time - start_time
    if delta.seconds == 0:
        return
    print(f'Requests rate is: {requests / delta.seconds} (requests per second)')


def run(address):
    global url
    url = address
    asyncio.run(start_clients())
