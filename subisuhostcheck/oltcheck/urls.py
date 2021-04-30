from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name="index"),
    #path('dashboard',views.dashboard,name="dashboard"),
    path('operational',views.operational,name="operational"),
    path('',views.down_list,name="downlist"),
    path('test',views.orm_test,name="test"),
    path('add',views.add_down_data,name="add"),
    #path('<int:id>',views.update_olt_data,name="updatedatas"),
    path('<int:id>/update',views.olt_update_form,name="updatedata"),
    path('olt',views.olt,name="olt"),
 
 
 
   #charts
    path('dashboard',views.google_charts,name="dashboard"),
]
