from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests

def index(request):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid=50f91fe67a5661be4a20aa945d246ba3')
    print(response.json())
    weather_obj = response.json()
    print(weather_obj['weather'][0])
    return render(request, 'weather/index.html', {
        "weather": weather_obj,
    })

def home(request):
    return HttpResponseRedirect('weather/')