import os
import threading


stri = '192.168.1.'

##def check_ip():
##    for i in range(160,170):
##        new_str =  stri + str(i)
##        print(new_str)
##        list.append(new_str)
##check_ip()
##print(list)
##
##uptime = []
##uptime_data= []
##
##def ping(f):
##    response = os.system(f"ping -n 1 {f}")
##    return response
##
##x= 0
##while x < 2:
##    with open("olttest.txt","r") as fname:
##        for f in fname:
##            thread = threading.Thread(target=ping, args=(f,))
##            thread.start()
##            response = ping(f)
##            if response == 0:
##                print(f"{f} is up\n")
##              
##            else:
##                print(f"{f} is down\n")
##                if f in uptime:
##                    continue
##                else:
##                    uptime.append(f)
##            x= x+1
##            print(x)
##print(uptime)
##


import concurrent.futures

hosts = ['ganamnagar','gthankot']
def ping(name):
    response = os.system(f"ping -n 1 {name}")
    if response == 0:
        print("up")

executor = concurrent.futures.ThreadPoolExecutor(254)
ping_hosts = [executor.submit(ping, str(ip)) for ip in hosts]
print(ping_hosts)

