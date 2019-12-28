from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    yrsold = models.DecimalField(max_digits=3,decimal_places=0)
    skills = models.CharField(max_length=50, blank=True)


class Feed_Message(models.Model):
    email = models.CharField(max_length=50, blank= True)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
