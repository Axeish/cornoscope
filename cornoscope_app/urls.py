from django.urls import path
from . import views

urlpatterns = [
    path('', views.horoscope_view, name='horoscope'),
    path('compatibility/', views.compatibility_view, name='compatibility'),
]