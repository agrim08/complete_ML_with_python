'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import multiprocessing.pool
import sys 
import math
import time

#increase numner of digit for integer conversion
sys.set_int_max_str_digits(100000)

#fucn for factorial:
def fact_clac(nums):
    print(f"calculating factorials of {nums}")
    res = math.factorial(nums)
    # print(f"factorial of {nums} is {res}")
    return res

if __name__ == "__main__":
    nums = [5000,6000,7000,8000]
    
    start_time = time.time()
    
    #create pool of worker process:
    '''The Pool class in Python's multiprocessing module is a powerful tool for parallel processing.
    It allows you to manage a pool of worker processes to which you can submit tasks.'''
    with multiprocessing.Pool() as pool:
        result = pool.map(fact_clac,nums)
    
    end_time = time.time()
    
    print(f"Results = {result}")
    print("time taken :",end_time-start_time)