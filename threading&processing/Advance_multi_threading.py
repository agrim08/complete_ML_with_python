from concurrent.futures import ThreadPoolExecutor
import time

def print_nums(nums):
    time.sleep(2)
    return f"Nums:- {nums}"

nums = [1,2,2,3,4,4,5,6]

with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(print_nums,nums)
    
for res in result:
    print(res)