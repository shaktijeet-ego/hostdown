from django.shortcuts import render

from . models import OvccData, OLT, Oltdown, Province

from django.db.models import Count

import os


# Create your views here.

# def index(request):
#     olt_data = OvccData.objects.all()
#     return render(request, 'index.html',{'olt_data':olt_data})

def dashboard(request):
    pass


from datetime import datetime

def index(request):
    olt_data = OvccData.objects.all()
    olt_down = Oltdown.objects.all().order_by('-downtime')
    #context = {'oltdown':olt_down}
    #total_uptime_olts = olt_data.filter(down_self=True).count()
    #total_olts = olt_data.filter(olt_name=1).count()
    hostname=OLT.objects.all()
    province = Province.objects.all()
    #for provinces in province:
        #pass
    #for hostname.objects.filter(province)
    for hostnames in hostname:
        response = os.system(f"ping -n 1 {hostnames}")
    #print(p)
    #print(type(response))
        if response==0:
            print(f"{hostnames} +  is up")
        else:
            print(f"{hostnames} +  is down")
            context = {'{hostnames}':hostname}
            if Oltdown.objects.filter(olt_name__contains = hostnames):
                #print(Oltdown.objects.filter(olt_name = hostnames))
                #print(f"{hostnames} already added")
                pass
            else:
                olt_down = Oltdown.objects.create(olt_name=str(hostnames),province=hostnames.province,downtime=datetime.now(),client_count=hostnames.client_count)
                olt_down.save()

    

    #olt_count = olt_data.count()
    #print(olt_count)
    #olt_data = OvccData.objects.filter("olt")

    return render(request, 'index.html',{'hostname':hostname,'oltdown':olt_down})

def update_olt_data(request, id):
    if request.method == 'Post':
        pi = Oltdown.objects.get(pk=id)
    return render(request,'update.html',{'id':id})

def down_list(request):
    olt_down = Oltdown.objects.all()
    #if Oltdown.objects.filter(uptime__isnull = True):
    context = {
        'olt_down':olt_down
        }
    #else:
        #pass
    return render(request, 'downlist.html',context)

# """ def olt_down(request):
#     p = subprocess.Popen('ping 192.168.0.110')
#     print(p) """

# def insert_olt_down(request):
#     hostname="test"
#     response = os.system(f"ping -n 1 {hostname}")
#     #print(p)
#     #print(type(response))
#     if response==0:
#         print(hostname + " is up")
#     else:
#         print(hostname + " is down")
#         olt_down = Oltdown.objects.create(name=hostname)
#         olt_down.save()




#########################################################################################
##################TEST CODE#################3

def orm_test(request):
    test_olt = OLT.objects.all()
    context = {
        "test_olt":test_olt
    }

    for test_olts in test_olt:
        print(test_olts.province)
    return render(request, 'test.html',context)