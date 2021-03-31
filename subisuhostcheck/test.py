import os

hostname=["chabahil","gchabahil","gthankot", "gtest","192.168.0.108","gtest2","gtest3"]
oltdown = []
for hostnames in hostname:
    response = os.system(f"ping -n 1 {hostnames}")
    if response==0:
        print(f"{hostnames} is up")
    else:
        print(f"{hostnames} is down")
        oltdown.append(hostnames)
print(oltdown)


for hostnames in oltdown:
    response = os.system(f"ping -n 1 {hostnames}")
    if response==0:
        print(f"{hostnames} is up")
    else:
        print(f"{hostnames} is down")
        if hostnames in oltdown:
            print("already added")
        else:
            oltdown.append(hostnames)
