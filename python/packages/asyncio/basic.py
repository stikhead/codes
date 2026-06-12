# Normally, Python code is synchronous
# If line 2 requires downloading a massive file, line 3 has to wait
# asyncio allows for concurrency. It lets your program say, "While I'm waiting for this file to download, let me go do other useful work

# async: Used to define a function as asynchronous (a "coroutine").
# await: Used inside an async function to pause execution until a task finishes, handing control back to the "Event Loop" to run other things.

import asyncio
import time

async def fetch_data(id):
    print(f"tasm {id}: starting to fetch data...")

    await asyncio.sleep(2)
    print(f"task {id}: done fetching data!")
    return f"data for {id}"


async def main():
    start_time = time.time()

    results = await asyncio.gather( # run three tasks concurrently
        fetch_data(1), # instead of taking 6 seconds it will take 2 seconds
        fetch_data(2),
        fetch_data(3)
    )

    print(f"all results: {results}")
    print(f"total time: {time.time() - start_time:.2f} seconds")

# We have to start the event loop to run async functions
asyncio.run(main())