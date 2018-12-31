from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from .models import *
import decimal
import urllib.request
import datetime
from django.utils import timezone 
from django.utils.timezone import is_aware, make_aware
from django.utils.dateparse import parse_date
from math import sin, cos, sqrt, atan2, radians

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
    offTime = request.GET.get('offTime', None)

    contr = Control.objects.get(control_id=int(1))

    try:
        if action == 'on':

            if not offTime:
                contr.set_off_time = None
            elif offTime == '0':
                contr.set_off_time = None
            elif offTime == '1':
                contr.set_off_time = timezone.now() + datetime.timedelta(minutes = 30)
            elif offTime == '2':
                contr.set_off_time = timezone.now() + datetime.timedelta(hours = 1)
            elif offTime == '3':
                contr.set_off_time = timezone.now() + datetime.timedelta(hours = 2)
            elif offTime == '4':
                contr.set_off_time = timezone.now() + datetime.timedelta(hours = 3)
            else:
                return HttpResponseBadRequest()

            contr.state = True
            contr.last_on_time = timezone.now()
            request1 = urllib.request.urlopen("http://192.168.0.120/?swi=1",timeout = 5)
        elif action == 'off':
            contr.state = False
            contr.last_off_time = timezone.now()
            contr.set_off_time = None
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

def farmList(request):

    mylat = request.GET.get('lat','')
    mylon = request.GET.get('lon','')

    hasGeo = False

    if not mylat == '' and not mylon == '':
        hasGeo = True
        mylat = radians(float(mylat))
        mylon = radians(float(mylon))

    # approximate radius of earth in km
    R = 6373.0

    farms = Farm.objects.all()

    dataList = list()
    for f in farms:

        d = 0
        if not mylat == '' and not mylon == '':
            lat = radians(f.location_lat)
            lon = radians(f.location_lng)

            dlon = mylon - lon
            dlat = mylat - lat

            a = sin(dlat / 2)**2 + cos(mylat) * cos(lat) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))

            distance = R * c
            d = round(distance,1)

            #return HttpResponse('d: '+ str(d))
        
        dataList.append({'farmObj': f, 'dist': d})
    
    context = {
        'dataList': dataList,
        'hasGeo': hasGeo,
    }

    #return HttpResponse('place: '+ place)
    return render(request, 'farm.html', context)