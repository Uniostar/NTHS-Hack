from django.contrib import admin
from .models import SensorData, checkData

# Register your models here.
admin.site.register(SensorData)
admin.site.register(checkData)