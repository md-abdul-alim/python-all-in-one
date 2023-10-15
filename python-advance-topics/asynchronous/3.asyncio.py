import asyncio
import aiohttp
import json


async def task_one():
    print("Task One is starting")
    await asyncio.sleep(3)
    print("Task One is complete")
    return "Task One is ok"


async def task_two():
    print("Task Two is starting")
    await asyncio.sleep(1)
    raise ValueError("Error in task two")


async def task_three():
    print("Task Three is starting")
    await asyncio.sleep(4)
    print("Task Three is complete")
    return 'Task Three is ok'


# Example 1 using asyncio.gather()
async def main():
    try:
        result = await asyncio.gather(
            task_one(),
            task_two(),
            task_three(),
            return_exceptions=True
        )  # Gather result in list
    except Exception as e:
        print(f"Caught an exception: {e}")
    else:
        print("Result: ", result)

print("----- Using asyncio.gather()-----")
asyncio.run(main())


# Example 2 using asyncio.wait()
async def main():
    tasks = [asyncio.create_task(task_one()), asyncio.create_task(task_two()), asyncio.create_task(task_three())]  # Can't pass the task directly since python3.8. Direct task pass will deprecate
    done, pending = await asyncio.wait(
        tasks,  # coroutine objects
        timeout=None,  # Don't use if you want to complete all task without time limit. Timeout parameter to wait for a maximum of 1 second for each of the task to complete. If the timeout is reached, we catch the asyncio.exceptions.TimeoutError exception. If any of the task complete within the specified time, we will cancel the remaining tasks that are still pending.
        # return_when=asyncio.FIRST_COMPLETED # Return when the first exception occurs
    )

    if pending:
        for task in pending:
            task.cancel()
    results = []
    for task in done:
        try:
            results.append(task.result())
        except Exception as e:
            print(f"Caught an exception: {e}")
    print(f"Success: {results}")

print("----- Using asyncio.wait() 1-----")
try:
    asyncio.run(main())
except asyncio.exceptions.TimeoutError:
    print("Timeout occurred!")
except asyncio.exceptions.CancelledError:
    pass


async def fetch(url):
    async with aiohttp.ClientSession() as session:  # This creates an asynchronous context manager, initiating a session for HTTP requests.
        async with session.get(url) as response:  # This asynchronously sends a GET request to the provided URL and waits for the response.
            return await response.text()  # It waits for and returns the response text (HTML content, in most cases).


# Example 3 using asyncio.wait()
async def fetch_url(url):
    try:
        # await asyncio.sleep(2)
        return await fetch(url)
    except Exception as e:
        raise ValueError(f"Error fetching {e}")


async def main():
    urls = ["https://machine.dekkoisho.com", "http://test.test"]

    tasks = [asyncio.create_task(fetch_url(url)) for url in urls]

    done, pending = await asyncio.wait(
        tasks,
        timeout=1,  # Set a timeout of 1 second for each task
        # return_when=asyncio.FIRST_EXCEPTION  # Return when the first exception occurs
    )

    for task in done:
        try:
            result = task.result()
            print(f"Success: {result}")
        except Exception as e:
            print(f"Exception: {e}")

    for task in pending:
        task.cancel()

print("----- Using asyncio.wait() 2-----")
try:
    asyncio.run(main())
except asyncio.exceptions.CancelledError:
    pass

'''
Summary of asyncio.gather() & asyncio.wait() function

Note: Below all decision may not True. 
From the above small test case for asyncio.gather() and asyncio.wait() get bellow:
    ~ gather()
    ~ gather() waits for all tasks to complete and returns their results or raises the first exception.
    ~ If gather()'s return_exceptions = False, then both gather() and wait() work same. Because if there raise any error, both stop further tasks and return
    ~ Primarily or The most important use of gather() is when we need all the results of the provided tasks. In this case return_exceptions = True is must. Otherwise it will stops the further tasks and return with error.   
    ~ Finally use gather(), when we have list of independent tasks that we want to run concurrently and collect the results afterward.

    ~ Wait()
    ~ wait() set individual timeouts for each task and handle exceptions separately
    ~ wait() will return only the successful tasks. Not any error result. In this case we will not able to understand why that task failed to complete task.
    ~ Set individual timeout of 1 second for each task and handle exceptions separately using asyncio.wait(). If any of the task failed, further tasks will terminate.
    ~ set return_when if you want to return when the first exception occurs. All tasks will not complete and raise error. Also there will be no return response if previous task succeed
    ~ return_when have 3 state: FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED. if not set, will default raise ValueError.
    ~ Handling Exceptions Individually: If you want to handle exceptions raised by coroutines individually and continue processing other tasks even if some of them raise exceptions, asyncio.wait() is better suited. You can use try and except blocks to catch exceptions for each task as they complete.

Visit this for more: https://chat.openai.com/share/3b5092fb-786c-408b-96b1-2d970baa79e9
'''


async def read_large_file(file):
    while True:
        line = await file.readline()
        if not line:
            break
        print("Line: ", line.decode().strip())


# async def main_():
#     file = await asyncio.open('async_large_file.txt', mode='rb')
#     await read_large_file(file)

"""
This snippet reads a large file line by line asynchronously, which is efficient and memory-friendly.
line = await file.readline(): Asynchronously reads a line from the file. It’s non-blocking, 
allowing other operations to proceed while waiting for the line to be read.
await asyncio.open('large_file.txt', mode='rb'): Asynchronously opens a file. 
This is particularly useful for large files where you don’t want to block the execution of the rest of your code while waiting for the file to open.
"""

# Topic - 6: Real-World Async Applications
print("------Real-World Async Applications------")


async def fetch_and_process(url):
    async with aiohttp.ClientSession() as session:  # Initiates an async session for making HTTP requests.
        async with session.get(url) as response:  # Asynchronously sends a GET request to the URL and waits for the response.
            data = await response.text()
            processed_data = json.loads(data)
            print(f"Data from {url}: {processed_data}")


async def main__():
    urls = ['https://api.example.com/data1', 'https://api.example.com/data2']
    tasks = [fetch_and_process(url) for url in urls]
    await asyncio.gather(*tasks)  # Runs all tasks concurrently, not sequentially.


# asyncio.run(main__())