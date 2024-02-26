from django.db import models
class Service(models.Model):
    uin=models.CharField(max_length=6)
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    ipaddress=models.CharField(max_length=12)
    macaddress=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
# Create your models here.cla
