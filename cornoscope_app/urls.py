from django.contrib import admin
from django.urls import path
from .views import HomePageView, HoroscopeDetailView, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home', HomePageView.as_view(), name='home'),
    path('horoscope/<str:sign>/', HoroscopeDetailView.as_view(), name='horoscope_detail'),

]