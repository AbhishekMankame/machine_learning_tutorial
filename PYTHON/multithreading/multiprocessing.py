## Multiprocessing - It allows us to create processes that runs in parallel
## When to use: CPU-Bound tasks --> tasks that are heavy on CPU usage (e.g., mathematical computations, data processing)
## Parallel execution - Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"{i*i*i}")

if __name__ == "__main__":
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Processrocess(target=cube_numbers)

    t=time.time()
    ## start the process
    p1.start()
    p2.start()

    ## wait for the process to complete
    p1.join()
    p2.join()

