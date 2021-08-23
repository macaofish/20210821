from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F

# Create your models here.
class Client(models.Model):
    short_name = models.CharField(max_length=16, null=False)
    long_name = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.short_name

class ContactPerson(models.Model):
    client = models.ForeignKey('Client', on_delete=models.SET(0))
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=30, null=True)

    @property
    def full_name(self):
        '''Return person's full name'''
        return '%s %s' % (self.first_name, self.last_name)