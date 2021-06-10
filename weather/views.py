import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Temperature
from geopy.geocoders import Nominatim
import time
import requests

def home(request):
    return HttpResponseRedirect('weather/')

@csrf_exempt
def new_search(request):

    if request.method == "POST":
        city = request.POST["content"]
        return HttpResponseRedirect('/weather/{}'.format(city))
    return HttpResponseRedirect('/weather/sycow')

@csrf_exempt
def city_search(request, city):
    geolocator = Nominatim(user_agent="weather")
    Temperature.objects.all().delete()
    location = geolocator.geocode(city)
    daily_api_link = 'https://api.openweathermap.org/data/2.5/onecall?lat='+str(location.latitude)+'&lon='+str(location.longitude)+'&units=metric&exclude=current&appid=50f91fe67a5661be4a20aa945d246ba3'
    api_link = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=50f91fe67a5661be4a20aa945d246ba3'
    print(daily_api_link)


    daily_weather_response = requests.get(daily_api_link)
    daily_obj = daily_weather_response.json()['hourly']

    current_weather_response = requests.get(api_link)
    weather_obj = current_weather_response.json()

    try:
        current_weather = {
            "city": weather_obj['name'],
            "temp": weather_obj['main']['temp'],
            "temp_min": weather_obj['main']['temp_min'],
            "temp_max": weather_obj['main']['temp_max'],
            "feels_like": weather_obj['main']['feels_like'],
            "pressure": weather_obj['main']['pressure'],
            "weather_main": weather_obj['weather'][0]['main'],
        }
        for n, day in enumerate(daily_obj):
            day_hour = time.ctime(int(day['dt']))[11:16]
            day_temp = day['temp']
            Temperature.objects.create(hour=day_hour,temp=day_temp)
    except:
        return HttpResponseRedirect('/')
    temp_obj = Temperature.objects.all()
    return render(request, 'weather/index.html', {
        "weather": current_weather,
        "qs": temp_obj,
    })

#def main(request):
#    return render(request, 'weather/main.html')