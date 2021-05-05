from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Temperature
import requests

def home(request):
    return HttpResponseRedirect('weather/')

@csrf_exempt
def new_search(request):
    temp_obj = Temperature.objects.all()
    try:
        city = request.POST["content"]
        api_link = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=50f91fe67a5661be4a20aa945d246ba3'
    except:
        api_link = 'http://api.openweathermap.org/data/2.5/weather?q=Twardogora&units=metric&appid=50f91fe67a5661be4a20aa945d246ba3'
    response = requests.get(api_link)
    weather_obj = response.json()
    try:
        front_obj = {
            "city": weather_obj['name'],
            "temp": weather_obj['main']['temp'],
            "temp_min": weather_obj['main']['temp_min'],
            "temp_max": weather_obj['main']['temp_max'],
            "feels_like": weather_obj['main']['feels_like'],
            "pressure": weather_obj['main']['pressure'],
            "weather_main": weather_obj['weather'][0]['main'],
        }
    except:
        return HttpResponseRedirect('/')
    return render(request, 'weather/index.html', {
        "weather": front_obj,
        "qs": temp_obj,
    })
