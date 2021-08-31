from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctors = models.CharField(max_length=150)  
    def __str__(self):
        return self.doctors

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name