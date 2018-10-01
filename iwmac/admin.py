from django.contrib import admin

from .models import Sensor


# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sensor._meta.get_fields()]


admin.site.register(Sensor, SensorAdmin)