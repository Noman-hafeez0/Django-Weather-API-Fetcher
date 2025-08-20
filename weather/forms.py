from django import forms
from .models import weather

class WeatherForm(forms.ModelForm):
    class Meta:
        model = weather
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter city name...'})
        }
