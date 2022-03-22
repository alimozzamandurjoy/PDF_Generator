from distutils.archive_util import make_zipfile
from django.db import models

# Create your models here.


class Profile(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    phone= models.CharField(max_length=100)
    summary= models.TextField(max_length=2000)
    degree= models.CharField(max_length=200)
    school = models.CharField(max_length=200,default='null')
    university= models.CharField(max_length=200)
    previous_work= models.CharField(max_length=1000)
    skills= models.TextField(max_length=1000)
    def __str__(self):
        return self.name