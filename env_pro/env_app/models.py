from django.db import models

# Create your models here.

class cloudtable(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=50,default="user@cloud.com")
    mobile=models.CharField(max_length=10,unique=True)