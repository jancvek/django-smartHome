from django.db import models

# Create your models here.
MEASURE_PLACES = (
    ('smasa','Soba Maša'),
    ('sspal','Soba spalnica'),
    ('kopal','Kopalnica'),
    ('kuhin','Kuhinja'),
    ('balkz','Balkon zahod'),
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