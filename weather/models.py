from django.db import models

# Create your models here.
class Temperature(models.Model):
    day = models.CharField(max_length=100)
    temp = models.FloatField()
    
    def __str__(self):
        return "{}-{}".format(self.day, self.temp)