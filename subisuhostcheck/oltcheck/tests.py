#from django.test import TestCase

# Create your tests here.

<<<<<<< HEAD
import threading
import time

# def func():
#     print('ran')
#     time.sleep(1)
#     print('done')
#     time.sleep(0.85)
#     print('donw')

# x = threading.Thread(target=func)
# x.start()
# print(threading.activeCount())
# time.sleep(1)
# print('fin')

# def count(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.01)
# for _ in range(2):
#     x = threading.Thread(target=count, args=(10,))
#     x.start()
# print("Done")

hostname = ('ganamnagar','gtest', 'gthankot','gthankot','gthankot','gthankot','gthankot','gthankot',)

import threading
import os
import time
start_time = time.time()
def worker(hostnames):
    response = os.system(f"ping -n 1 {hostnames}")
    if response == 0:
        print(f"{hostnames} isup")
    else:
        print(f"{hostnames} is down")
thread_list = []
for hostnames in hostname:
    thread = threading.Thread(target=worker, args=(hostnames,))
    thread_list.append(thread)
    thread.start()

print(thread_list)
print(threading.activeCount())


print("--- %s seconds ---" % (time.time() - start_time))
=======


import time
from concurrent.futures import ThreadPoolExecutor

import os

img_url = ["ganamnagar","gthamel","gthankot","gtest"]

def download_images(url):
    test = os.system("ping -n 1 ganamnagar")
    print(test)
    

start = time.perf_counter() #start timer
with ThreadPoolExecutor() as executor:
    results = executor.map(download_images,img_url) #this is Similar to map(func, *iterables)
finish = time.perf_counter() #end timer
print(f"Finished in {round(finish-start,2)} seconds")
>>>>>>> dropdown


