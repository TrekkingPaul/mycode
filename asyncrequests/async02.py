#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Demonstrating how to use the asyncio library by utilizing the pokeapi.co
   to perform 150 HTTP GET lookups"""

# standard library
import asyncio
import time

# python3 -m pip install aiohttp
import aiohttp


async def make_request(session, pokemon_url):
    # the coroutine we are defining should be run async with an event loop
    async with session.get(pokemon_url) as resp:
        response = await resp.json()
        print(response["name"])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for number in range(1, 152):
            # Create a task for each of our requests
            task = asyncio.create_task(
                make_request(session, f"https://pokeapi.co/api/v2/pokemon/{number}")
            )
            tasks.append(task)
            
        # Run awaitable objects (tasks) concurrently
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))

