from django.contrib import admin

# Register your models here.
from .models import vinfo,cooling_system

admin.site.register(vinfo)
admin.site.register(cooling_system)