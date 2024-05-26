from django.shortcuts import render

from django.shortcuts import render
from .models import Horoscope, Compatibility

def horoscope_view(request):
    horoscopes = Horoscope.objects.all()
    return render(request, 'cornoscope_app/horoscope.html', {'horoscopes': horoscopes})

def compatibility_view(request):
    compatibilities = Compatibility.objects.all()
    return render(request, 'cornoscope_app/compatibility.html', {'compatibilities': compatibilities})