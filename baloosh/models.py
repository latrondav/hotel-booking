from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=200,)

    def __str__(self):
        return str(self.name)

class Bookings(models.Model):
    arrivaldates = models.CharField(max_length=200, null=False, blank=False)
    departuredates = models.CharField(max_length=200, null=False, blank=False)
    adults = models.CharField(max_length=200, null=False, blank=False)
    children = models.CharField(max_length=200, null=False, blank=False)
    noofrooms = models.CharField(max_length=200, null=False, blank=False)
    roomtypes = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return str(self.roomtypes)
    

