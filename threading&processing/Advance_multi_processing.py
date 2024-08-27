from concurrent.futures import ProcessPoolExecutor
import time

def sq_nums(nums):
    time.sleep(2)
    return f"Squre :- {nums*nums}"

nums = [1,2,3,4,5,6,7,8,89,14]

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(sq_nums, nums)
    
    for res in result:
        print(res)