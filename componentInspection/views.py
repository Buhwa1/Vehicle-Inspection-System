from django.shortcuts import render
from .models import vinfo,cooling_system

# Create your views here.
def carform(request):
    if request.method == "POST":
        # 
        # Cooling_system = cooling_system()
        stickerno = request.POST['stickernumber']
        date = request.POST['date']
        location = request.POST['location']
        mda = request.POST['mda']
        regno = request.POST['regno']
        engineno = request.POST['engineno']
        chassisno = request.POST['chassisno']
        year = request.POST['year']
        make = request.POST['make']
        mileage = request.POST['mileage']
        vehicletype = request.POST['type']
        radiator = request.POST['radiatorcondition']
        fan = request.POST['fancondition']
        ac = request.POST['ac']
        belts = request.POST['belts']
        horsepipes = request.POST['horsepipes']

        Vinfo = vinfo(stickerno=stickerno,date=date,location=location,mda=mda,
        regno=regno,engineno=engineno,chassisno=chassisno,year=year,
        make=make,mileage=mileage,vehicletype=vehicletype
        )
        Vinfo.save()
        #  = stickerno
        # vinfo.date = date
        # vinfo.location = location
        # vinfo.mda = mda
        # vinfo.regno = regno
        # vinfo.engineno = engineno
        # vinfo.chassisno = chassisno
        # vinfo.year = year
        # vinfo.make = make
        # vinfo.mileage = mileage
        # vinfo.vehicletype = vehicletype
        Vinfo.save()
        # last_id = vinfo.objects.last().id
        obj = vinfo.objects.latest('id')
        # cid = vinfo.objects.get(id=pk)
        Cooling_system = cooling_system(vehicleID=obj,radiatorcondition=radiator,fan=fan,ac=ac,
       belts=belts,horsepipes=horsepipes
       )
        
        Cooling_system.save()

    return render(request,"componentInspection/index.html")