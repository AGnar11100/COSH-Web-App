from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsItem, Event
from .weather.key import apiKey
import requests
import numpy as np


def convert_temp_and_get_icon_url(weather_data):
    temp_kelvin = weather_data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'
    return np.ceil(temp_fahrenheit).astype(int), icon_url

def home(request):
    # Fetch news items and calendar events
    newsItems = NewsItem.objects.all()
    calendarEvents = Event.objects.all().order_by('start_datetime')

    # Fetch weather data
    city = "Santa Cruz"
    state = "CA"
    country = "US"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={apiKey}'
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temp_fahrenheit, icon_url = convert_temp_and_get_icon_url(weather_data)
        weather = {
            'temperature': temp_fahrenheit,
            'icon_url': icon_url
        }
    else:
        weather = {'error': 'Failed to retrieve weather data'}

    # Pass all data to the template
    context = {
        'newsItems': newsItems,
        'calendarEvents': calendarEvents,
        'weather': weather
    }
    return render(request, 'core/core.html', context)