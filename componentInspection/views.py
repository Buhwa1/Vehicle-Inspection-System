from django.shortcuts import render
from .models import brakes, vinfo,cooling_system, exhaust, engine, frame, lights, safe_loading, steering_mechanism, suspension, tires, wheels, transmission, windshield, windows, rating

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
        servicebrakes = request.POST['servicebrakes']
        parkingbrakes = request.POST['parkingbrakes']
        electricbrakes = request.POST['electricbrakes']
        hydraulicbrakes = request.POST['hydraulicbrakes']
        vacuum= request.POST['vacuum']
        brakedrum = request.POST['brakedrum']
        pressurewarning= request.POST['pressurewarning']
        tractorprotection= request.POST['tractorprotection']
        aircompressor = request.POST['aircompressor']
        systemcondition= request.POST['systemcondition']
        sensorcondition = request.POST['sensorcondition']
        oillevel = request.POST['oillevel']
        visibleleaks= request.POST['visibleleaks']
        generaloperation = request.POST['generaloperation']
        framemembers = request.POST['framemembers']
        wheelclearance= request.POST['wheelclearance']
        axleassemblies = request.POST['axleassemblies']
        vehiclebody = request.POST['vehiclebody']
        bodypaints= request.POST['bodypaints']
        crossmembers = request.POST['crossmembers']
        lumpLH = request.POST['lumpLH']
        lumpRH = request.POST['lumpRH']
        indicatorFLH= request.POST['indicatorFLH']
        indicatorRRH = request.POST['indicatorRRH']
        brakeRH = request.POST['brakeRH']
        reverseRH= request.POST['reverseRH']
        parkinglights = request.POST['parkinglights']
        bedcondition= request.POST['bedcondition']
        bucketcondition = request.POST['bucketcondition']
        doorhinges = request.POST['doorhinges']
        bedhingesRH= request.POST['bedhingesRH']
        bedhingesLH = request.POST['bedhingesLH']
        steeringplay = request.POST['steeringplay']
        steeringcolumn= request.POST['steeringcolumn']
        frontaxlebeam = request.POST['frontaxlebeam']
        steeringgear= request.POST['steeringgear']
        pitmanarm = request.POST['pitmanarm']
        powersteering = request.POST['powersteering']
        balljoints = request.POST['balljoints']
        tierod= request.POST['tierod']
        steeringnuts = request.POST['steeringnuts']
        ubolts= request.POST['ubolts']
        bushes = request.POST['bushes']
        springassembly = request.POST['springassembly']
        tongue = request.POST['tongue']
        radius= request.POST['radius']
        tracking = request.POST['tracking']
        frontRH = request.POST['frontRH']
        frontLH = request.POST['frontLH']
        rearRH = request.POST['rearRH']
        rearLH= request.POST['rearLH']
        sparetire = request.POST['sparetire']
        lockring = request.POST['lockring']
        wheelsandrims = request.POST['wheelsandrims']
        fasteners = request.POST['fasteners']
        nuts = request.POST['nuts']
        welds = request.POST['welds']
        clutchassembly = request.POST['clutchassembly']
        gearbox = request.POST['gearbox']
        propellershaft= request.POST['propellershaft']
        drivingshafts = request.POST['drivingshafts']
        wind = request.POST['wind']
        blades = request.POST['blades']
        mouldings= request.POST['mouldings']
        wipermotors = request.POST['wipermotors']
        motorsRHF = request.POST['motorsRHF']
        motorsRHR = request.POST['motorsRHR']
        motorsLHF = request.POST['motorsLHF']
        motorsLHR= request.POST['motorsLHR']
        glasscondition = request.POST['glasscondition']
        poor = request.POST['poor']
        fair= request.POST['fair']
        good = request.POST['good']
        



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

        Brake_system = brakes(vehicleID=obj,servicebrakes=servicebrakes,parkingbrakes=parkingbrakes,electricbrakes=electricbrakes,hydraulicbrakes=hydraulicbrakes,vacuum=vacuum,brakedrum=brakedrum,pressurewarning=pressurewarning,tractorprotection=tractorprotection,aircompressor=aircompressor)
        Brake_system.save()

        Exhaust_system = exhaust(vehicleID = obj,systemcondition=systemcondition,sensorcondition=sensorcondition)
        Exhaust_system.save()

        Engine = engine(vehicleID = obj,oillevel=oillevel,visibleleaks=visibleleaks,generaloperation=generaloperation)
        Engine.save()

        Frame = frame(vehicleID = obj,framemembers=framemembers,wheelclearance=wheelclearance,axleassemblies=axleassemblies,vehiclebody=vehiclebody,bodypaints=bodypaints,crossmembers=crossmembers)
        Frame.save()

        Lighting_devices = lights(vehicleID = obj,lumpLH=lumpLH,lumpRH=lumpRH,indicatorFLH=indicatorFLH,indicatorRRH=indicatorRRH,brakeRH=brakeRH,reverseRH=reverseRH,parkinglights=parkinglights)
        Lighting_devices.save()

        Safe_loading = safe_loading(vehicleID =obj,bedcondition=bedcondition,bucketcondition=bucketcondition,doorhinges=doorhinges,bedhingesRH=bedhingesRH,bedhingesLH=bedhingesLH)
        Safe_loading.save()

        Steering_mechanism = steering_mechanism(vehicleID =obj,steeringplay=steeringplay,steeringcolumn=steeringcolumn,frontaxlebeam=frontaxlebeam,steeringgear=steeringgear,pitmanarm=pitmanarm,powersteering=powersteering,balljoints=balljoints,tierod=tierod,steeringnuts=steeringnuts)
        Steering_mechanism.save()

        Suspension = suspension(vehicleID=obj,ubolts=ubolts,bushes=bushes,springassembly=springassembly,tongue=tongue,radius=radius,tracking=tracking)
        Suspension.save()

        Tires = tires(vehicleID=obj,frontRH=frontRH,frontLH=frontLH,rearRH=rearRH,rearLH=rearLH,sparetire=sparetire)
        Tires.save()

        Wheels = wheels(vehicleID=obj,lockring=lockring,wheelsandrims=wheelsandrims,fasteners=fasteners,nuts=nuts,welds=welds)
        Wheels.save()

        Transmission = transmission(vehicleID=obj,clutchassembly=clutchassembly,gearbox=gearbox,propellershaft=propellershaft,drivingshafts=drivingshafts)
        Transmission.save()

        Windshield = windshield(vehicleID=obj,wind=wind,blades=blades,mouldings=mouldings,wipermotors=wipermotors)
        Windshield.save()

        Windows = windows(vehicleID=obj,motorsRHF=motorsRHF,motorsRHR=motorsRHR,motorsLHF=motorsLHF,motorsLHR=motorsLHR,glasscondition=glasscondition)
        Windows.save()

        Rating = rating(vehicleID=obj,poor=poor,fair=fair,good=good)
        Rating.save()

    return render(request,"componentInspection/index.html")