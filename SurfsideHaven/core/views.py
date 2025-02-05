from django.shortcuts import render
from django.utils import timezone
from .models import NewsItem, Event
# from .weather.key import apiKey # For development only
import requests
import numpy as np
import os

def convert_temp_and_get_icon_url(weather_data):
    temp_kelvin = weather_data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f'http://openweathermap.org/img/w/{icon_code}.png'
    return np.ceil(temp_fahrenheit).astype(int), icon_url

def home(request):
    # Get today's date and time
    now = timezone.now()

    # Fetch calendar events that start today or later
    calendarEvents = Event.objects.filter(start_datetime__gte=now).order_by('start_datetime')

    # Fetch weather data
    city = "Santa Cruz"
    state = "CA"
    country = "US"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={os.getenv("COSH_WEATHER_API_HERO")}'
    
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
        'newsItems': NewsItem.objects.all(),  # unchanged, all news items are fetched
        'calendarEvents': calendarEvents,
        'weather': weather
    }
    return render(request, 'core/core.html', context)
