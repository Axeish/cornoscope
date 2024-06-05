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

