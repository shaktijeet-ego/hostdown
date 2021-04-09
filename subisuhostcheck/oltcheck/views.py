from django.shortcuts import render, redirect, get_object_or_404

from . models import  OLT, Oltdown, Province

from django.db.models import Count, F

import os
import threading
import time


# Create your views here.

# def index(request):
#     olt_data = OvccData.objects.all()
#     return render(request, 'index.html',{'olt_data':olt_data})

def dashboard(request):
    pass


from datetime import datetime
from django.utils import timezone

def threading_hosts(hostnames):
    response = os.system(f"ping -n 1 {hostnames}")
    time.sleep(2)
    olt_down = Oltdown.objects.all().order_by('-downtime')
    hostname = OLT.objects.all()
    province = Province.objects.all()
    for provinces in province:
        pass
    #print(f"**********************************{response}****")
    if response==0:
        for olt_downs in olt_down:
            if Oltdown.objects.filter(olt_name__contains = hostnames) & Oltdown.objects.filter(uptime__isnull = True):
                Oltdown.objects.filter(id=olt_downs.id).update(uptime=timezone.now())
            
                #print(olt_downs.id)
            #Oltdown.objects.filter(uptime__isnull = True).update(uptime= datetime.now())
    else:
        print(f"{hostnames} +  is down")
        
        if Oltdown.objects.filter(olt_name__contains = hostnames) & Oltdown.objects.filter(uptime__isnull = True):
            print(f"{hostnames} already added")
        else:
            olt_down = Oltdown.objects.create(olt_name=str(hostnames),
            province=hostnames.province,
            downtime=timezone.now(),
            client_count=hostnames.client_count,
            category=None,
            )
            olt_down.save()
            
    


def index(request):
    #olt_data = OvccData.objects.all()
    olt_down = Oltdown.objects.all().order_by('-downtime')
    #context = {'oltdown':olt_down}
    #total_uptime_olts = olt_data.filter(down_self=True).count()
    #total_olts = olt_data.filter(olt_name=1).count()
    hostname = OLT.objects.all()
    
    #province = Province.objects.all()
    #for provinces in province:
        #pass
    #for hostname.objects.filter(province)

    for hostnames in hostname:
        thread = threading.Thread(target=threading_hosts, args=(hostnames,))
        thread.start()
        #print(p)
        #print(type(response))
        response = threading_hosts(hostnames)
        #print(f"**********************************{response}****")
        if response==0:
            if Oltdown.objects.filter(olt_name__contains = hostnames) & Oltdown.objects.filter(uptime__isnull = True):
                pass
                #Oltdown.objects.filter(uptime__isnull = True).update(uptime= datetime.now())
        else:
            print(f"{hostnames} +  is down")
            context = {'{hostnames}':hostname}
            if Oltdown.objects.filter(olt_name__contains = hostnames) & Oltdown.objects.filter(uptime__isnull = True):
                print(f"{hostnames} already added")
            else:
                olt_down = Oltdown.objects.create(olt_name=str(hostnames),
                province=hostnames.province,
                downtime=datetime.now(),
                client_count=hostnames.client_count,
                category=None,
                )
                olt_down.save()


    return render(request, 'index.html',{'hostname':hostname,'oltdown':olt_down})

    

from .forms import OltDownForm

def olt_update_form(request,id):
    context={}

    obj = get_object_or_404(Oltdown,id=id)
    form = OltDownForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    context["form"] = form


    return render(request,"update.html",context)

def update_olt_data(request, id):
    if request.method == 'Post':
        pi = Oltdown.objects.get(pk=id)
        
    return render(request,'update.html',{'id':id})

def down_list(request):
    olt_down = Oltdown.objects.all()
    hostnames = OLT.objects.all()
    #if Oltdown.objects.filter(uptime__isnull = True):
    context = {
        'olt_down':olt_down
        }
    #else:
        #pass
    return render(request, 'downlist.html',context)

#FOR OPERATIONAL VIEW

def operational(request):
    olt_down = Oltdown.objects.filter(reason__exact='')
    context={
        'olt_down':olt_down
    }
    return render(request, 'operational.html',context)

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