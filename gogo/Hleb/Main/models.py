from django.db import models
from datetime import datetime

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title 

class Docs(models.Model):
    name = models.CharField(max_length=300)
    speciality = models.CharField(max_length=20)
    door = models.CharField(max_length=5)
    equipment = models.BooleanField(default=False)

class Visits(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now=True)
    patient = models.CharField(max_length=300)
    comment = models.TextField(blank=True)

class Patient(models.Model):
    name = models.CharField(max_length=300)
    adress = models.CharField(max_length=300)


class Visitt(models.Model):
    date = models.DateTimeField(auto_now=True)
    patientt = Patient.name
    doc = Docs.name






