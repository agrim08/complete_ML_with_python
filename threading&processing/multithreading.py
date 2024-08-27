import time
import threading

def call_num():
    for i in range(5):
        time.sleep(2)
        print(f"number{i}")

def call_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"letter{letter}")

# start_time = time.time()
# call_num()
# call_letters()
# final_time = time.time() - start_time
# print(final_time)

'''What if i dont want to wait for call_num to execute completely, and want to execute call_letters
    we can use multi threading
'''

#creating threads
t1 = threading.Thread(target=call_num)
t2 = threading.Thread(target=call_letters)

#starting thread
start_time = time.time()
t1.start()
t2.start()

#wait for thread to complete:
t1.join()
t2.join()

final_time = time.time() - start_time
print(final_time)