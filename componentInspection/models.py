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

class brakes(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    servicebrakes = models.CharField(max_length=30)
    parkingbrakes = models.CharField(max_length=30)
    electricbrakes = models.CharField(max_length=30)
    hydraulicbrakes = models.CharField(max_length=30)
    vacuum = models.CharField(max_length=30)
    brakedrum = models.CharField(max_length=30)
    pressurewarning = models.CharField(max_length=30)
    tractorprotection = models.CharField(max_length=30)
    aircompressor = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class exhaust(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    systemcondition = models.CharField(max_length=30)
    sensorcondition = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class engine(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    oillevel = models.CharField(max_length=30)
    visibleleaks = models.CharField(max_length=30)
    generaloperation = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class frame(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    framemembers = models.CharField(max_length=30)
    wheelclearance = models.CharField(max_length=30)
    axleassemblies = models.CharField(max_length=30)
    vehiclebody = models.CharField(max_length=30)
    bodypaints = models.CharField(max_length=30)
    crossmembers = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class lights(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    lumpLH = models.CharField(max_length=30)
    lumpRH = models.CharField(max_length=30)
    indicatorFLH = models.CharField(max_length=30)
    indicatorRRH = models.CharField(max_length=30)
    brakeRH = models.CharField(max_length=30)
    reverseRH = models.CharField(max_length=30)
    parkinglights = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class safe_loading(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    bedcondition = models.CharField(max_length=30)
    bucketcondition = models.CharField(max_length=30)
    doorhinges = models.CharField(max_length=30)
    bedhingesRH = models.CharField(max_length=30)
    bedhingesLH = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class steering_mechanism(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    steeringplay = models.CharField(max_length=30)
    steeringcolumn = models.CharField(max_length=30)
    frontaxlebeam = models.CharField(max_length=30)
    steeringgear = models.CharField(max_length=30)
    pitmanarm = models.CharField(max_length=30)
    powersteering = models.CharField(max_length=30)
    balljoints = models.CharField(max_length=30)
    tierod = models.CharField(max_length=30)
    steeringnuts = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class suspension(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    ubolts = models.CharField(max_length=30)
    bushes = models.CharField(max_length=30)
    springassembly = models.CharField(max_length=30)
    tongue = models.CharField(max_length=30)
    radius = models.CharField(max_length=30)
    tracking = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)


class tires(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    frontRH = models.CharField(max_length=30)
    frontLH = models.CharField(max_length=30)
    rearRH = models.CharField(max_length=30)
    rearLH = models.CharField(max_length=30)
    sparetire = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class wheels(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    lockring = models.CharField(max_length=30)
    wheelsandrims = models.CharField(max_length=30)
    fasteners = models.CharField(max_length=30)
    nuts = models.CharField(max_length=30)
    welds = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class transmission(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    clutchassembly = models.CharField(max_length=30)
    gearbox = models.CharField(max_length=30)
    propellershaft = models.CharField(max_length=30)
    drivingshafts = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class windshield(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    wind = models.CharField(max_length=30)
    blades = models.CharField(max_length=30)
    mouldings = models.CharField(max_length=30)
    wipermotors = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class windows(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    motorsRHF = models.CharField(max_length=30)
    motorsRHR = models.CharField(max_length=30)
    motorsLHF = models.CharField(max_length=30)
    motorsLHR = models.CharField(max_length=30)
    glasscondition = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID)

class rating(models.Model):
    vehicleID = models.ForeignKey(vinfo, on_delete=models.CASCADE,null=True,blank=True)
    poor = models.CharField(max_length=30)
    fair = models.CharField(max_length=30)
    good = models.CharField(max_length=30)

    def __str__(self):
        return str(self.vehicleID) 