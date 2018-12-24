from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .models import *
import decimal
import urllib.request
from datetime import datetime
from django.utils import timezone

from time import sleep

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
        testValue = request.GET.get('test','')
        return HttpResponse('Test request... OK')

    return HttpResponse('Test request... ERROR!')

def roomTemp(request, place=''):
    
    #set default place
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
        'myJson' : json_data,
    }

    #return HttpResponse('place: '+ place)
    return render(request, 'room_temperature.html', context)

def control(request):

    contr = Control.objects.get(control_id=int(1))
    state = contr.state
    desc = contr.description
    onTime = contr.last_on_time

    context = {
        'state': state,
        'desc': desc,
        'onTime': onTime,
    }

    return render(request, 'control.html', context)

def ajaxTest(request):
    action = request.GET.get('action', None)

    contr = Control.objects.get(control_id=int(1))

    try:
        if action == 'on':
            contr.state = True
            contr.last_on_time = timezone.now()
            request1 = urllib.request.urlopen("http://192.168.0.120/?swi=1",timeout = 5)
        elif action == 'off':
            contr.state = False
            contr.last_off_time = timezone.now()
            request1 = urllib.request.urlopen("http://192.168.0.120/?swi=0",timeout = 5)
        else:
            return HttpResponseBadRequest()

        requestStatus = request1.getcode()
        #print(request1.getcode())
        #print(request1.read())
    except urllib.error.HTTPError as e:
        return HttpResponseServerError()
        #print(e.code)
        #print(e.read()) 
    #handle timeout
    except urllib.error.URLError as e:
        return HttpResponseServerError()
        #print(e.reason)   

    #save data in model only if there is no error
    contr.save()

    data = {
        'status': requestStatus,
        'text': '',
    }

    return JsonResponse(data)