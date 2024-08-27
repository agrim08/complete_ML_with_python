import multiprocessing
import time

def sq_num():
    for i in range(5):
        time.sleep(1)
        print(f"sqaure:{i*i}")

def cube_num():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube:{i**3}")

if __name__ == " __main__":
    
    p1 = multiprocessing.Process(target=sq_num)
    p2 = multiprocessing.Process(target=cube_num)
    t=time.time()

    #start the process
    p1.start()
    p2.start()
    
    #wait for process to start
    p1.join()
    p2.join()

    final_time = time.time()
    print(final_time - t)

