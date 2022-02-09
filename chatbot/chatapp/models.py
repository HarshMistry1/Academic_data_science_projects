from django.db import models

# Create your models here.
class chatdata(models.Model):
    name=models.CharField(max_length=50,default=None)
    msg=models.TextField(default=None)
    reply=models.TextField(default=None)
    
    def __str__(self):
        return self.name
class chat(models.Model):
    msg=models.CharField(max_length=200)
