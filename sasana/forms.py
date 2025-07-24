from django import forms
from .models import Sasana

class SasanaForm(forms.ModelForm):
    class Meta:
        model = Sasana
        fields = '__all__'
