from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Horoscope, Compatibility


class Index(View):
    def get(self,request):

        return render(request, 'index.html')
class HomePageView(View):
    def get(self, request):
        horoscopes = Horoscope.objects.all()
        return render(request, 'home.html', {'horoscopes': horoscopes})

class HoroscopeDetailView(View):
    def get(self, request, sign):
        horoscope = get_object_or_404(Horoscope, sign=sign)
        return render(request, 'horoscope_detail.html', {'horoscope': horoscope})
def compatibility_view(request):
    compatibilities = Compatibility.objects.all()
    return render(request, 'cornoscope_app/compatibility.html', {'compatibilities': compatibilities})