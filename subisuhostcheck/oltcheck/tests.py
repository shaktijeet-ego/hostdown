#from django.test import TestCase

# Create your tests here.



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


