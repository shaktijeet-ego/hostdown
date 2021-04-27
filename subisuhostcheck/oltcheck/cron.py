from django.shortcuts import render, redirect, get_object_or_404

from . models import  OLT, Oltdown, Province
from django.http import HttpResponse
from django.db.models import Count, F

import os
import threading
import time
from datetime import datetime
from django.utils import timezone

def threading_hosts(hostnames):
    response = os.system(f"ping -c 1 {hostnames}")
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
            
            
    


def cron_olt():
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

    for hostnames in hostname[364:]:
        thread = threading.Thread(target=threading_hosts, args=(hostnames,))
        thread.start()
        #print(p)
        #print(type(response))
        #response = threading_hosts(hostnames)
    context = {'{hostnames}':hostname}
        
    return 'success'