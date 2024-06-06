# myapp/urls.py
from django.urls import path
from .views import SetDateOfBirthView, TooYoungView, HomePageView, HoroscopeDetailView, compatibility_view

urlpatterns = [
    path('', SetDateOfBirthView.as_view(), name='index'),  # Form page
    path('home/', HomePageView.as_view(), name='home'),
    path('too-young/', TooYoungView.as_view(), name='too_young'),
    path('horoscope/<str:sign>/', HoroscopeDetailView.as_view(), name='horoscope_detail'),
    path('compatibility/', compatibility_view, name='compatibility'),
]
