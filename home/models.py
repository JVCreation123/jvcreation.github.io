from pyexpat import model
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=10)
    phone = models.CharField(max_length=12)
    date = models.DateField()

    def __str__(self):
        return self.name