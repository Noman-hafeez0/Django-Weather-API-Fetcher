# 🌤️ Weather API Fetcher (Django)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django&logoColor=white)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

A simple yet powerful **Weather Application** built with **Django** that fetches real-time weather data using the **OpenWeatherMap API**.  
You can **add cities**, **view live weather conditions**, and **delete cities** when no longer needed.

---

## ✨ Features
- 🔍 Search and add any city to track weather.  
- 🌡️ View **temperature, description, and weather icons** in real time.  
- 🗑️ Remove cities from your dashboard.  
- ⚠️ Handles **invalid city names** with error messages.  
- 🎨 Clean, responsive, and user-friendly interface.  

---

🛠️ Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS (Bootstrap/ optional)

API: OpenWeatherMap

Database: SQLite (default, can switch to PostgreSQL/MySQL)


## Must Setp up your Virtual Enviroment

python -m venv venv    
source venv/bin/activate   # Linux / Mac    
venv\Scripts\activate      # Windows     

# Virtual Enviroment (Custom)
use requiremets txt file provided within

pip install -r requirements.txt


# Use an API Key 
(you can get a custom free API key from openweatherapp.org ) just Signup

🎯 Usage

Enter a city name in the input box.

Click Add City → Weather info appears in dashboard.

To remove a city, just click the ❌ Delete button.

#📂 Project Structure

weather_app/    
│-- weather/           # Django app (models, views, urls)    
│-- templates/         # HTML templates      
│-- manage.py    
│-- requirements.txt    
│-- README.md    




