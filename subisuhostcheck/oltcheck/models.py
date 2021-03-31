from django.db import models

# Create your models here.

class Province(models.Model):
    province = models.CharField(max_length = 25)

    def __str__(self):
        return self.province

class ClientCount(models.Model):
    client_count = models.CharField(max_length = 25)

    def __str__(self):
        return self.client_count

class OLT(models.Model):
    olt_name = models.CharField(max_length = 25)
    province = models.ForeignKey(Province,on_delete = models.CASCADE)
    client_count = models.ForeignKey(ClientCount,on_delete = models.CASCADE)

    def __str__(self):
        return self.olt_name





class Category(models.Model):
    category = models.CharField(max_length = 25)

    def __str__(self):
        return self.category

class Reason(models.Model):
    reason = models.CharField(max_length = 25)
    

    def __str__(self):
        return self.reason


class OvccData(models.Model):
    olt_name = models.ForeignKey(OLT,on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete = models.CASCADE)
    downtime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField()
    #Duration
    informed_to = models.CharField(max_length = 25)
    reason = models.ForeignKey(Reason, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    down_self = models.BooleanField(default = True)

    def __str__(self):
        return str(self.olt_name)

class Oltdown(models.Model):
    olt_name = models.CharField(max_length = 25)
    province = models.ForeignKey(Province, on_delete = models.CASCADE)
    downtime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(null = True)
    informed_to = models.CharField(max_length = 25)
    reason = models.CharField(max_length = 25)
    category = models.CharField(max_length = 25)
    down_self = models.BooleanField(default = True)
    client_count = models.ForeignKey(ClientCount, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.olt_name)


    