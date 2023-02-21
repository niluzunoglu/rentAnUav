from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    brandName = models.CharField(null=False,max_length=40)
    
class BrandModel(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    modelName = models.CharField(null=False,max_length=50)
    
class Category(models.Model):
    categoryName = models.CharField(max_length=40)

class UAV(models.Model):
    
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    
    created_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=User.objects.first().pk)
    
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=False)
    brandModel = models.ForeignKey(BrandModel,on_delete=models.CASCADE,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    flightHours = models.FloatField(null=True)
    payload = models.FloatField(null=True)
    wingspan = models.FloatField(null=True)
    maxSpeed = models.FloatField(null=True)
    length = models.FloatField(null=True)
    endurance = models.FloatField(null=True)
    
    additionalNotes = models.TextField(max_length=200,null=True)
    
    class Meta:
        db_table = "uav"
    