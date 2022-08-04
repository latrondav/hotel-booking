from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    message = models.TextField(max_length=200,)

    def __str__(self):
        return str(self.name)

class Reservations(models.Model):
    arrivaldates = models.CharField(max_length=200, null=False, blank=False)
    departuredates = models.CharField(max_length=200, null=False, blank=False)
    adults = models.CharField(max_length=200, null=False, blank=False)
    children = models.CharField(max_length=200, null=False, blank=False)
    noofrooms = models.CharField(max_length=200, null=False, blank=False)
    roomtypes = models.CharField(max_length=200, null=False, blank=False)
    amounts = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return str(self.name)

    def calc(self, *args, **kwargs):
        if self.roomtypes == "SSR":
            self.amounts = self.noofrooms * 100
        elif self.roomtypes == "DSR":
            self.amounts = self.noofrooms * 200
        elif self.roomtypes == "TSR":
            self.amounts = self.noofrooms * 300
        elif self.roomtypes == "QSR":
            self.amounts = self.noofrooms * 400
        elif self.roomtypes == "QuSR":
            self.amounts = self.noofrooms * 500
        elif self.roomtypes == "KSR":
            self.amounts = self.noofrooms * 600
        elif self.roomtypes == "TwSR":
            self.amounts = self.noofrooms * 700
        elif self.roomtypes == "StSR":
            self.amounts = self.noofrooms * 800
        elif self.roomtypes == "SDR":
            self.amounts = self.noofrooms * 900
        elif self.roomtypes == "DDR":
            self.amounts = self.noofrooms * 1000
        elif self.roomtypes == "HS":
            self.amounts = self.noofrooms * 120
        elif self.roomtypes == "ES":
            self.amounts = self.noofrooms * 2000
        else:
            self.amounts = 0
        
        return super.calc(self, *args, **kwargs)