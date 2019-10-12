from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    mail = models.EmailField(max_length=100)
    gender = models.BooleanField()