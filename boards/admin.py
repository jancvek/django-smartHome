from django.contrib import admin

# Register your models here.
from .models import OnlineData
from .models import HouseData
from .models import Device
from .models import Control

admin.site.register(OnlineData)
admin.site.register(HouseData)
admin.site.register(Device)
admin.site.register(Control)