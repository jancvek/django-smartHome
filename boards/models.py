from django.db import models

# Create your models here.
MEASURE_PLACES = (
    ('smasa','Soba Maša'),
    ('sspal','Soba spalnica'),
    ('kopal','Kopalnica'),
    ('kuhin','Kuhinja'),
    ('balkz','Balkon zahod'),
    ('zdnev','Dnevna zgoraj'),
)

class HouseData(models.Model):
    measure_place = models.CharField(max_length=5, choices=MEASURE_PLACES) 
    temp = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    humidity = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    save_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        retStr = str(self.save_time) + " - " + str(self.measure_place)
        return str(retStr)

class OnlineData(models.Model):
    MEASURE_PLACES = (
        ('KRA',"Kranj"),
        ('NAK',"Naklo"),
        ('TRZ',"Tržič"),
        ('LLE','Letališče Lesce'),
    )
    measure_place = models.CharField(max_length=3, choices=MEASURE_PLACES)
    temp = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    humidity = models.IntegerField(null=True)
    rain_prob = models.IntegerField(null=True)
    clouds = models.IntegerField(null=True)
    save_time = models.DateTimeField(auto_now_add=True)

class Device(models.Model):
    dev_ident = models.IntegerField(null=False)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    measure_place = models.CharField(max_length=5, choices=MEASURE_PLACES)
    rssi = models.IntegerField(null=True, blank=True)
    measure_delay = models.IntegerField(null=True, blank=True)

    def __str__(self):
        retStr = str(self.dev_ident) + " - " + str(self.name)
        return str(retStr)

class Control(models.Model):
    control_id = models.IntegerField(null=False)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=False)
    state = models.BooleanField()
    last_on_time = models.DateTimeField(null=True, blank=True)
    last_off_time = models.DateTimeField(null=True, blank=True)
    set_off_time = models.DateTimeField(null=True, blank=True)
    wan_ip = models.CharField(null=True, max_length=32)

    def __str__(self):
        retStr = str(self.control_id) + " - " + str(self.name)
        return str(retStr)

class Farm(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=64, blank=True)
    contact = models.TextField(blank=True)
    location_lat = models.FloatField(null=True, blank=True, default=None)
    location_lng = models.FloatField(null=True, blank=True, default=None)
    
    def __str__(self):
        retStr = str(self.name)
        return str(retStr)

class Offer(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    quantity = models.CharField(max_length=16, blank=True)
    price = models.FloatField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='test/', blank=True, null=True)
    farm = models.ForeignKey(Farm, related_name='offers', on_delete=models.CASCADE)

    def __str__(self):
        retStr = str(self.name)
        return str(retStr)