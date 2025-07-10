## Multithreading
## When to use multithreading
### I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
### Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently. 

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        print(f"Letter: {letter}")

t=time.time()
print_numbers()
print_letter()
finished_time=time.time()-t
print(finished_time)