from django.db import models
from django.contrib.auth.models import User


class Belongs(models.Model):
    user = models.OneToOneField(User,related_name="belong",related_query_name="belong",null=True,blank=True,on_delete=models.CASCADE)
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default = False)

class Cities(models.Model):
    name=models.CharField(max_length=100,default="enter")
    def __str__(self):
        return self.name


class otherDetails(models.Model):
    user = models.OneToOneField(User,related_name="details",related_query_name="details",null=True,blank=True,on_delete=models.CASCADE)
    address=models.TextField(max_length=250, blank=True)
    phonenumber=models.IntegerField(default=9898944)
    city=models.ForeignKey(Cities,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.address




