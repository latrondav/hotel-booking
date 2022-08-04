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
    amounts = models.CharField(max_length=200, null=False, blank=False)

    def get_amounts(self):
        if self.roomtypes == "SSR":
            result = int(self.noofrooms * 100)
        elif self.roomtypes == "DSR":
            result = int(self.noofrooms * 200)
        elif self.roomtypes == "TSR":
            result = int(self.noofrooms * 300)
        elif self.roomtypes == "QSR":
            result = int(self.noofrooms * 400)
        elif self.roomtypes == "QuSR":
            result = int(self.noofrooms * 500)
        elif self.roomtypes == "KSR":
            result = int(self.noofrooms * 600)
        elif self.roomtypes == "TwSR":
            result = int(self.noofrooms * 700)
        elif self.roomtypes == "StSR":
            result = int(self.noofrooms * 800)
        elif self.roomtypes == "SDR":
            result = int(self.noofrooms * 1000)
        elif self.roomtypes == "DDR":
            result = int(self.noofrooms * 1200)
        elif self.roomtypes == "HS":
            result = int(self.noofrooms * 1400)
        elif self.roomtypes == "ES":
            result = int(self.noofrooms * 2000)
        else:
            result = int(0)
        
        return result

    def save(self, *args, **kwargs):
        self.amounts = self.get_amounts()
        super(Bookings, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.user)

