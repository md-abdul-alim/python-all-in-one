import time
from multiprocessing import Pool, cpu_count, Queue, Manager, Process

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
