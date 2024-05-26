from django import forms
from .models import Horoscope


class UploadXMLForm(forms.Form):
    xml_file = forms.FileField(label='Upload XML File', required=True)

