# Processes that run in parallel
# When to use:
    # cpu bound tasks
    # task that are heavy on cpu usage (e.g., mathematical computations, data processing).
    # parallel execution - multiple cores of the cpu

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__":

    # create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    # set a timer
    t = time.time()

    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    # execution time
    et = time.time() - t

    print(f"execution time: {et}")

# to execute this code use this format instead of code runner extension
# python 016-Python-Multi-Threading-and-Multi-Processing/003-multi-threading-practical-implementation.py