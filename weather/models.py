from django.db import models

# Create your models here.
class Temperature(models.Model):
    hour = models.CharField(max_length=100)
    temp = models.FloatField()
    
    def __str__(self):
        return "{}-{}".format(self.hour, self.temp)