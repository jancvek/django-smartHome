from django.contrib import admin

# Register your models here.
from .models import OnlineData
from .models import HouseData
from .models import Device

admin.site.register(OnlineData)
admin.site.register(HouseData)
admin.site.register(Device)