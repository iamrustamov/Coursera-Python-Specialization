# asyncio, async def / await; PEP 492 Python3.5

import asyncio


async def hello_world():
    while True:
        print("Hello world")
        await asyncio.sleep(1.0)


loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
