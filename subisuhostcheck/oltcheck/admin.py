from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(OLT)
admin.site.register(Province)
admin.site.register(Category)
admin.site.register(Reason)
#admin.site.register(OvccData)
admin.site.register(Oltdown)
admin.site.register(ClientCount)

