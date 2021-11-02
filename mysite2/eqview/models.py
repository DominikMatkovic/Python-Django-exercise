from django.db import models


class Person(models.Model):
    OIB = models.CharField(unique=True,max_length=11)
    def __str__(self):
        return self.OIB

class Equipment(models.Model):
    serialNum = models.CharField(unique=True,max_length=100)
    borrowedBy = models.ForeignKey(Person, on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):     
        return self.serialNum