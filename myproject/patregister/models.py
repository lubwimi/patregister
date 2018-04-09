from django.contrib.auth.models import User
from django.db import models

class Patmos(models.Model):
    fornamn = models.CharField(max_length=255)
    efternamn = models.CharField(max_length=255)
    personnummer = models.CharField(max_length=15)
    adress = models.TextField()
    telefon = models.CharField(max_length=30)
    #fodelsedatum = models.CharField(max_length=50)
    dopdatum = models.CharField(max_length=50)
    ankomstdatum = models.CharField(max_length=50)
    uttrade = models.CharField(max_length=50)
    gift_med = models.CharField(max_length=50)
    ogift = models.CharField(max_length=50)
    
    def __str__(self):
        return self.fornamn
    

