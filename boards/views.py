from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from .models import *
import decimal

def home(request):

    oDataKranj = OnlineData.objects.filter(measure_place="KRA")
    oDataTrzic = OnlineData.objects.filter(measure_place='TRZ')

    #tn = datetime.datetime.now()
    #x = datetime.datetime(tn.year, tn.month, tn.day)

    objList = list()
    for kObj in oDataKranj:
        objDic = {"temp1": kObj.temp}
        objList.append(objDic)

    i = 0
    for tObj in oDataTrzic:
        objList[i].update({"temp2": tObj.temp, "time": tObj.save_time})
        i += 1

    choices = list()
    for x in MEASURE_PLACES:
        choices.append(x[1])

    return render(request, 'home.html', {'testTemp': objList, 'choices': choices})
    

def input(request):

    if request.method == 'GET':
        moduleId = request.GET['module_id']
        temp = request.GET['temp']
        humidity = request.GET['humi']
        rssi = request.GET['rssi']
        
        #return HttpResponse('Send request... module_id: '+moduleId+' temp: '+temp+' humi: '+humidity)

        if not moduleId:
            return HttpResponse('Send request... ERROR!')

        #get device place
        device = Device.objects.get(dev_ident=int(moduleId))
        measureDelay = device.measure_delay

        measurePlace = device.measure_place
        newData = HouseData(measure_place=measurePlace)

        if temp:
            tempDec = decimal.Decimal(temp)
            newData.temp = '{0:0.1f}'.format(tempDec)

        if humidity:
            humiDec = decimal.Decimal(humidity)
            newData.humidity = '{0:0.1f}'.format(humiDec)

        if rssi:
            device.rssi = int(rssi)
            device.save()

        #save data to db
        newData.save()

        return HttpResponse('Send request... OK delay:'+str(measureDelay))
    
    return HttpResponse('Send request... ERROR!')

def checkConn(request):
    if request.method == 'GET':
        testValue = request.GET['test']
        return HttpResponse('Test request... OK')

    return HttpResponse('Test request... ERROR!')

def roomTemp(request, place=''):
    if not place:
        return redirect('/smasa/')

    query = HouseData.objects.filter(measure_place=place)

    latest = query.last()

    choices = list()
    for x in MEASURE_PLACES:
        choices.append({'key': x[0], 'value': x[1]})

    json_data = serializers.serialize("json", query)    
    context = {
        'temp': query,
        'choices': choices,
        'curr_place': place,
        'latest': latest,
        "myJson" : json_data,
    }

    #return HttpResponse('place: '+ place)
    return render(request, 'room_temperature.html', context)