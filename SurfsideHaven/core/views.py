from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsItem, Event

def home(request):
    newsItems = NewsItem.objects.all()
    calendarEvents = Event.objects.all().order_by('start_datetime')
    return render(request, 'core/core.html', {'newsItems': newsItems, 'calendarEvents': calendarEvents})
