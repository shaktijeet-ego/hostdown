from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('downlist',views.down_list,name="downlist"),
    path('test',views.orm_test,name="test"),
    path('<int:id>',views.update_olt_data,name="updatedatas"),
    path('<int:id>/update',views.olt_update_form,name="updatedata"),
]
