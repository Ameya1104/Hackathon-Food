from django.db import models
from django.contrib.auth.models import User


class Belongs(models.Model):
    user = models.OneToOneField(User, related_name="belong", related_query_name="belong", null=True, blank=True,
                                on_delete=models.CASCADE)
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)


class Cities(models.Model):
    name = models.CharField(max_length=100, default="enter")

    def __str__(self):
        return self.name


class otherDetails(models.Model):
    user = models.OneToOneField(User, related_name="details", related_query_name="details", null=True, blank=True,on_delete=models.CASCADE)
    address = models.TextField(max_length=250, blank=True)
    phonenumber = models.IntegerField(default=9898944123)
    image=models.ImageField(upload_to='NGO/images')
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.address


class Measurement(models.Model):
    name = models.CharField(max_length=100, default="enter")

    def __str__(self):
        return self.name

class TypeOf(models.Model):
    name = models.CharField(max_length=100, default="enter")

    def __str__(self):
        return self.name
class foodAvbl(models.Model):
    user = models.ForeignKey(User, related_name="foodss", related_query_name="foodss", null=True, blank=True,on_delete=models.CASCADE)
    otherDetails = models.OneToOneField(otherDetails, null=True, blank=True, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, null=True)
    typee = models.ForeignKey(TypeOf, on_delete=models.CASCADE, null=True,default="veg")
    quantity = models.IntegerField()
    Other_Specifics=models.TextField(max_length=100,default="Punjabi,Chinese,Mexican")
    images=models.ImageField(upload_to='NGO/images', null=True, blank=True)
    city = models.CharField(max_length=100, default="enter")
    pickup_address = models.TextField(max_length=20)
    created_on=models.DateTimeField(auto_now_add=False , editable=True,null=True)
    edible = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)
