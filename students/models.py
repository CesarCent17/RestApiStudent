from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    contact = models.EmailField()

    