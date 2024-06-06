from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from datetime import datetime

from .models import Horoscope, Compatibility

class SetDateOfBirthView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        dob_str = request.POST.get('dob')
        gender = request.POST.get('gender')
        try:
            dob = datetime.strptime(dob_str, '%d/%m/%Y').date()
            today = datetime.today().date()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                return redirect('too_young')
            request.session['date_of_birth'] = dob_str
            request.session['gender'] = gender
            return redirect('home')
        except ValueError:
            return render(request, 'index.html', {'error': 'Invalid date format. Please use DD/MM/YYYY.'})
class TooYoungView(View):
    def get(self, request):
        return render(request, 'too_young.html')


class HomePageView(View):
    def get(self, request):
        dob_str = request.session.get('date_of_birth')
        if dob_str:
            dob = datetime.strptime(dob_str, '%d/%m/%Y')
            sign = self.calculate_zodiac_sign(dob.month, dob.day)
            horoscopes = Horoscope.objects.all()
            horoscope = Horoscope.objects.filter(sign=sign).first()
            if horoscope:
                return render(request, 'home.html', {'dob':dob_str,'horoscope': horoscope, 'horoscopes': horoscopes})
        # If date of birth is not set or zodiac sign not found, render without horoscope
        return render(request, 'home.html', {'dob':dob_str,'horoscope': "invalid", 'horoscopes': horoscopes})

    def calculate_zodiac_sign(self, month, day):
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return 'Aquarius'
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return 'Pisces'
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return 'Aries'
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return 'Taurus'
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return 'Gemini'
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return 'Cancer'
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return 'Leo'
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return 'Virgo'
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return 'Libra'
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return 'Scorpio'
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return 'Sagittarius'
        else:
            return 'Capricorn'
# class HomePageView(View):
#
#     def get(self, request):
#         horoscopes = Horoscope.objects.all()
#         return render(request, 'home.html', {'horoscopes': horoscopes})

class HoroscopeDetailView(View):
    def get(self, request, sign):
        horoscope = get_object_or_404(Horoscope, sign=sign)
        return render(request, 'horoscope_detail.html', {'horoscope': horoscope})

def compatibility_view(request):
    compatibilities = Compatibility.objects.all()
    return render(request, 'cornoscope_app/compatibility.html', {'compatibilities': compatibilities})
