from django.db import models

# Create your models here.
class vinfo(models.Model):
    stickerno = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    mda = models.CharField(max_length=30)
    regno = models.CharField(max_length=30)
    engineno = models.CharField(max_length=30)
    chassisno = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    mileage = models.CharField(max_length=30)
    vehicletype = models.CharField(max_length=30)

    def __str__(self):
        return self.regno

class cooling_system(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    radiatorcondition = models.CharField(max_length=30)
    fan = models.CharField(max_length=30)
    ac = models.CharField(max_length=30)
    belts = models.CharField(max_length=30)
    horsepipes = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)