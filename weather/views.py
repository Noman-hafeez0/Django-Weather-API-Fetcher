import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages   # 👈 needed for alerts
from .forms import WeatherForm
from .models import weather   # 👈 your model (lowercase "w"? maybe rename to Weather later)

def index(request):
    api_key = '' #Put Your API Key Here to make it Work
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']   # 👈 take name from form
            r = requests.get(url.format(city_name, api_key)).json()

            if r.get("cod") == 200:   # ✅ valid city
                if not weather.objects.filter(name__iexact=city_name).exists():  # 👈 check duplicates
                    form.save()
                    messages.success(request, f"✅ {city_name} added successfully!")
                else:
                    messages.warning(request, f"⚠️ {city_name} already exists.")
            else:
                messages.error(request, f"❌ City '{city_name}' not found!")

    form = WeatherForm()
    cities = weather.objects.all()
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name, api_key)).json()

         

        city_weather = {
            'id': city.id,
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'index.html', context)


def delete_city(request, city_id):
    city = get_object_or_404(weather, id=city_id)
    messages.info(request, f"🗑️ {city.name} removed.")
    city.delete()
    return redirect('home')
