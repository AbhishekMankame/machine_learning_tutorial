### Multithreading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers = [1,2,3,4,5,6,7,8,9,10,1,11,21,123]

with ThreadPoolExecutor(max_workers=2) as executor:
    results=executor.map(print_number,numbers)

for result in results:
    print(result)