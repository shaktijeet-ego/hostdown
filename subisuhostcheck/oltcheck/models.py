from django.db import models

# Create your models here.

COLOR_CHOICES = (
    ('RF Duty Managers','RF Duty Managers'),
    ('SPR', 'SPR'),
    ('Province Team','Province Team'),
    ('L2','L2'),
    ('Power','Power'),
)

class Province(models.Model):
    province = models.CharField(max_length = 25)

    def __str__(self):
        return self.province

# class ClientCount(models.Model):
#     client_count = models.CharField(max_length = 25)

    # def __str__(self):
    #     return self.client_count

class OLT(models.Model):
    olt_name = models.CharField(max_length = 25)
    province = models.ForeignKey(Province,on_delete = models.CASCADE)
    client_count = models.CharField(max_length = 25, blank = True)

    def __str__(self):
        return self.olt_name





class Category(models.Model):
    category = models.CharField(max_length = 25)

    def __str__(self):
        return self.category

class Reason(models.Model):
    reason = models.CharField(max_length = 25)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    

    def __str__(self):
        return self.reason


# class OvccData(models.Model):
#     olt_name = models.ForeignKey(OLT,on_delete=models.CASCADE)
#     province = models.ForeignKey(Province, on_delete = models.CASCADE)
#     downtime = models.DateTimeField(auto_now=True)
#     uptime = models.DateTimeField()
#     #Duration
#     informed_to = models.CharField(max_length = 25)
#     reason = models.ForeignKey(Reason, on_delete = models.CASCADE)
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)
#     down_self = models.BooleanField(default = True)

#     def __str__(self):
#         return str(self.olt_name)

OLT_Choices = (('test','test'),)

class Oltdown(models.Model):
    olt_name = models.CharField(max_length = 25)
    province = models.ForeignKey(Province, on_delete = models.CASCADE)
    downtime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(blank=True, null = True)
    informed_to = models.CharField(max_length = 25,choices=COLOR_CHOICES )
    reason = models.CharField(max_length = 25, default = "", blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True, null=True)
    down_self = models.BooleanField(default = True)
    client_count = models.CharField(max_length = 2000, blank = True, null = True)

    def __str__(self):
        return str(self.olt_name)


    