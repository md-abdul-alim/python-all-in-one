"""
Reference: https://www.linkedin.com/pulse/asynchronous-programming-asyncawait-asyncio-elshad-karimov/
"""
import time
import json
import asyncio
import aiohttp
from multiprocessing import Pool, cpu_count, Queue, Manager, Process

"""
Asynchronous
-----asyncio
---------~Gather ::
---------------return all response including error response in one response. so can't cancel unsuccessful tasks.
---------~Wait :: 
---------------return completed tasks and and pending tasks separately. so pending tasks can be canceled. 
-----multiprocessing
----------~Pool :: simple way to run worker process. can't sync between two process.
---------------~map :: 
------------------------- used for parallel execution of a function on multiple input values.
------------------------- takes an iterable as input like list and passed the function
------------------------- return a list of results
------------------------- return results according to the order of input
---------------~apply :: 
------------------------- used for single set of arguments in parallel. It doesn't operate on an iterable like map
------------------------- take a single function and its arguments as input.
------------------------- return a single result
------------------------- no result order as this is a single set of arguments
----------~Process :: more control over the processes. can sync data between two processes
--------------------if failed to complete any task, we can get error cause.
"""


# Topic - 1. Basic async/await Usage
async def main():
    print("Hello")
    await asyncio.sleep(1)  # This 1 second other tasks will perform, await will not prevent any blockage in code execution for this 1 second.
    print("World")

asyncio.run(main())


# Topic - 2. asyncio with aiohttp
async def fetch(url):
    async with aiohttp.ClientSession() as session:  # This creates an asynchronous context manager, initiating a session for HTTP requests.
        async with session.get(url) as response:  # This asynchronously sends a GET request to the provided URL and waits for the response.
            return await response.text()  # It waits for and returns the response text (HTML content, in most cases).


async def main():
    try:
        html = await fetch('https://machine.dekkoisho.com') # Calls the fetch() function and waits for it to complete, storing the returned text
        # print(html)
    except Exception as e:
        print('Error: ', e)

asyncio.run(main())


# Topic - 3. Concurrency with asyncio
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

# Topic - 4. Parallelism with multiprocessing
print("------multiprocessing example 1------")


def calculate_square(x):
    return x*x


if __name__ == '__main__':
    with Pool(5) as pool:
        print(pool.map(calculate_square, [1, 2, 3, 4, 5]))


print("------multiprocessing example 2 - Pool Map()------")


def multi_task_one():
    return 999999*99999*999999*999999


def multi_task_two():
    return 999999*99999*999999*999999


if __name__ == '__main__':
    tasks = [multi_task_one(), multi_task_two()]
    print("Total available cpu cores: ", cpu_count())

    # Create a multiprocessing Pool with 6 processes (adjust as needed)
    pool = Pool(processes=6)

    # Use the pool.map function to distribute the work among processes
    results = pool.map(calculate_square, tasks)

    # Close the pool and with for the work to finish
    pool.close()
    pool.join()

    # Print the results
    print("Pool Map: ", results)

print("------multiprocessing example 2 - Pool Apply()------")


# Function to calculate the square of a number
def calculate_square(number):
    return number * number


if __name__ == "__main__":
    pool = Pool(processes=4)

    numbers = [1, 2, 3, 4, 5]

    # Use pool.apply() to calculate squares in parallel
    results = [pool.apply(calculate_square, args=(num,)) for num in numbers]
    print("Pool Apply: ", results)

    pool.close()
    pool.join()

    for num, result in zip(numbers, results):
        print(f"The square of {num} is {result}")

print("------multiprocessing example 3 - Pool Map() & Apply()------")

if __name__ == "__main__":
    with Pool(processes=2) as pool:
        # Using pool.map() to square elements of an iterable
        result_map = pool.map(calculate_square, [1, 2, 3, 4, 5])
        print("pool.map() result:", result_map)

        # Using pool.apply() to square a single value
        result_apply = pool.apply(calculate_square, (11,))
        print("pool.apply() result:", result_apply)

print("------multiprocessing.Queue() example 4 ------")
'''
Sharing data and communication between processes
We have two processes: one that produces data and another that consumes the data using multiprocessing.Queue()
'''

# Function that runs in a separate process and raises an exception


def worker():
    try:
        print("Worker process: Starting work...")
        time.sleep(2)
        print("Worker process: Raising an exception...")
        # Simulate an error (division by zero)
        result = 1 / 0
    except Exception as e:
        print(f"Worker process: Exception raised: {str(e)}")


def producer(q):
    for i in range(1, 6):
        q.put(f"Data {i}")
        print(f"Produced: Data {i}")


def consumer(q):
    while True:
        data = q.get()
        if data is None:
            break
        print(f"Consumed: {data}")


if __name__ == "__main__":
    q = Queue()

    producer_process = Process(target=producer, args=(q,))
    consumer_process = Process(target=consumer, args=(q,))
    worker_process = Process(target=worker)

    # Start the processes
    producer_process.start()
    consumer_process.start()

    print("Producer process alive: ", producer_process.is_alive())
    # Wait for the producer to finish
    producer_process.join()

    # Signal the consumer to stop. After data finished in queue, it will wait, because consumer on while true. So set none to say there is no more data
    # q.put(None)
    consumer_process.terminate()
    # consumer_process.join()

    # Check process is alive or not
    print("Producer process alive: ", producer_process.is_alive())
    print("Consumer process alive: ", consumer_process.is_alive())

    # Testing error handling using join() after terminate()
    worker_process.start()
    time.sleep(1)
    worker_process.terminate()
    worker_process.join()  # Use join() to get the reason of termination of that process

    print("Worker process alive: ", worker_process.is_alive())

    # Check if the process raised an exception
    if worker_process.exitcode != 0:
        print(f"Main program: Worker process terminated with exit code {worker_process.exitcode}")
    else:
        print("Main program: Worker process completed without exceptions.")

    print("Main program exiting.")

print("------multiprocessing.Manager() example 4 ------")
'''
Create a shared list that multiple process can modify
'''


# Function to append data to a shared list
def append_data(shared_list, data):
    shared_list.append(data)
    print(f"Append: {data}")


if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list()

        process1 = Process(target=append_data, args=(shared_list, "Data 1"))
        process2 = Process(target=append_data, args=(shared_list, "Data 2"))

        # Start the processes
        process1.start()
        process2.start()

        # Wait for the processes to finish
        process1.join()
        process2.join()

        # Print the contents of the shared list
        print("Shared List: ", shared_list)
'''
Summary of multiprocessing pool:
    ~ pool.close(): This method is used to prevent any more tasks from being submitted to the pool. After calling
        pool.close(), we can't add more tasks to the pool. It essentially signals that the pool should not accept
         any new tasks but should continue processing the existing ones.
    ~ pool.join(): This method is used to wait for all the worker processes in the pool to complete their tasks
        and terminate. It blocks the main program's execution until all the tasks in the pool are finished.
        This ensures that the main program won't exit before the pool has completed its work.
    ~ processes: Process indicated the number of worker processes to use. Each process will be run on a separate
        CPU core, enabling parallel execution.
    ~ pool.map(): This maps ensure that each task being processed by a separate process.
    ~ cpu_count(): Creating more processes than the available cores might not lead to better performance.
        So check the available cores.
    ~ Pool Vs Process
        ~ Pool() for simple way to run worker process
        ~ Process() for more control over process creation and management and flexibility.
    ~ start(): Start child process
    ~ join(): Wait until child process terminates. The program will block until that process has finished executing.
        Here are some potential consequences of not using join():
            ~ if we don't use join(), process doesn't is_active=False. It's True. So to end the process join() is necessary.
            ~ Unpredictable Execution Order: The order in which processes complete their execution is not guaranteed. Without join(), the main program may continue running and potentially complete before one or more subprocesses finish their work.
            ~ Incomplete Work: If the main program depends on the results of subprocesses, it might access incomplete or uninitialized data if it proceeds without waiting for subprocesses to complete.
            ~ Resource Leaks: If a subprocess spawns additional subprocesses or allocates resources that should be cleaned up when it's finished, not using join() can result in resource leaks.
            ~ Control Flow Issues: Without proper synchronization, it can be challenging to coordinate and control the flow of your program when it involves multiple subprocesses.
            ~ In summary, using join() is crucial for proper coordination and synchronization of processes in a multiprocessing program. It ensures that the main program waits for all subprocesses to finish their work before continuing, helping to maintain order, reliability, and data consistency in your multi-process applications.
    ~ terminate(): used to forcefully terminate a running process.
    ~ q.put(None) & consumer_process.terminate() both work same. Both signal to terminate the process.
    ~ Why we should use join() after terminate() though it is not necessary?
        ~ Cleanup: terminate() does not allow the process to perform any cleanup operations. If the terminated process had acquired resources, opened files, or allocated memory, those resource might not be properly released without cleanup.
            By using join(), we can give the terminated process an opportunity to perform any necessary cleanup operations before if fully exits.
        ~ Error Handling: During terminate if errors occur, use join() to wait and finish then check exit status that why the error happened.
Note:
    ~ try to avoid global variables.
Use case:
    ~ Each of the processes is run in parallel, which is especially useful for CPU-bound 
        tasks where operations are computationally expensive.
    ~ We can take advantage of multiple CPU cares to process the data more efficiently whe dealing with large 
        datasets or computationally intensive tasks.
'''


# Topic - 5. Advanced asyncio
async def read_large_file(file):
    while True:
        line = await file.readline()
        if not line:
            break
        print("Line: ", line.decode().strip())


async def main_():
    file = await asyncio.open('async_large_file.txt', mode='rb')
    await read_large_file(file)

# asyncio.run(main_())
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