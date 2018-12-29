from django.contrib import admin

# Register your models here.
from .models import OnlineData
from .models import HouseData
from .models import Device
from .models import Control
from .models import Farm
from .models import Offer

admin.site.register(OnlineData)
admin.site.register(HouseData)
admin.site.register(Device)
admin.site.register(Control)
admin.site.register(Farm)
admin.site.register(Offer)