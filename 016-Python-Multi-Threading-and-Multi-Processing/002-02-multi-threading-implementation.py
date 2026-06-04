# Multithreading
# When to use multi threading
# I/O bound task: Tasks that spend more time waiting for I/O operations (e.g., file operations, network request).
# Concurrent execution: when you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        # the reason i use sleep, let's assume there is an io operation perform here
        time.sleep(2)
        print(f"Number: {i}")
    print()

def print_letters():
    for letter in "abcd":
        time.sleep(1)
        print(f"Letter: {letter}")
    print()

# create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)


# run in parallelly

t = time.time()
# start the thread
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()
# 
exe_time = time.time()-t

print(f"start time: {t}")
print(f"execution time: {exe_time}")