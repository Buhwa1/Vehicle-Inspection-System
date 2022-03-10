from django.contrib import admin

# Register your models here.
from .models import engine, exhaust, frame, lights, rating, safe_loading, steering_mechanism, suspension, tires, transmission, vinfo,cooling_system,brakes, wheels, windows, windshield

admin.site.register(vinfo)
admin.site.register(cooling_system)
admin.site.register(brakes)
admin.site.register(exhaust)
admin.site.register(engine)
admin.site.register(frame)
admin.site.register(lights)
admin.site.register(safe_loading)
admin.site.register(steering_mechanism)
admin.site.register(suspension)
admin.site.register(tires)
admin.site.register(wheels)
admin.site.register(transmission)
admin.site.register(windshield)
admin.site.register(windows)
admin.site.register(rating)
