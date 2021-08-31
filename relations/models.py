from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Student_Profile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    roll = models.CharField(max_length=80)

    def __str__(self):
        return self.student.name