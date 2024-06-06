from django import forms
from .models import Horoscope
from django.core.exceptions import ValidationError
from datetime import date

GENDER_CHOICES = (
    (0, 'Other'),
    (1, 'Gay Man'),
    (2, 'Lesbian'),
)


class UploadXMLForm(forms.Form):
    xml_file = forms.FileField(label='Upload XML File', required=True)

class DateOfBirthForm(forms.Form):
    dob = forms.DateField(label='Date of Birth', input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'))

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError("You must be at least 18 years old to use this service.")
        return dob

class GenderForm(forms.Form):
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)