from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.menu)