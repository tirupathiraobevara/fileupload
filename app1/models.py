from django.db import models
class Student(models.Model):
    Stdno=models.IntegerField()
    Stdname=models.CharField(max_length=40)
    ProfPic=models.FileField(blank=True,null=True)
    StdAdd=models.CharField(max_length=40)
# Create your models here.
