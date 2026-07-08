from datetime import datetime
from dotenv import load_dotenv
import os
import requests
search_history = []
load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.openweathermap.org/data/2.5/weather"
url = "https://api.openweathermap.org/data/2.5/forecast"
def current_weather():
    city = input("Enter the City: ")
    params = {
        "q" : city,
        "appid" :  API_KEY, 
        "units" : "metric"
    }
    response = requests.get(url,params = params)
    weather = response.json()
    if response.status_code == 404:
        print("=" * 40)
        print("City Not Found!")
        print("Please Enter a Valid City.")
        print("=" * 40)
        return
    sunrise = datetime.fromtimestamp(weather["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(weather["sys"]["sunset"])
    if city not in search_history:
        search_history.append(city)
    print("=" * 40)
    print(f"📍 City         : {weather['name']}")
    print(f"🌡 Temperature   : {weather['main']['temp']:.1f} °C")
    print(f"💧 Humidity     : {weather['main']['humidity']}%")
    print(f"🌬 Wind Speed    : {weather['wind']['speed']} m/s")
    print(f"☁ Weather       : {weather['weather'][0]['description'].title()}")
    print(f"🌡️ Feels like    : {weather["main"]["feels_like"]:.1f} °C ")
    print(f"🗜 Pressure      : {weather["main"]["pressure"]} hPa ")
    print(f"👀 Visibility   : {weather["visibility"]/1000} km")
    print(f"🌅 Sunrise      : {sunrise.strftime('%I:%M %p')}")
    print(f"🌇 Sunset       : {sunset.strftime('%I:%M %p')}")
    print("=" * 40)
def clear_screen():
    os.system("cls")
def view_history():
    print("=" * 12, "Search History", "=" * 12)
    if not search_history:
        print("No Searches Yet")
        print("=" * 40)
        return
    for index, search in enumerate(search_history, start = 1):
        print(f"{index}. {search.capitalize()}")
    print("=" * 40)
def weather_forecast():
    city = input("Enter the city: ")
    params = {
        "q" : city,
        "appid" :  API_KEY, 
        "units" : "metric"
    }
    response = requests.get(url,params = params)
    forecast = response.json()
    for forecast_data in forecast["list"]:
        if "12:00:00" in forecast_data["dt_txt"]:
            print("=" * 40)
            date = datetime.strptime(forecast_data["dt_txt"],"%Y-%m-%d %H:%M:%S")
            print(date.strftime("%A, %d %b"))
            print(f"🌡  Temperature : {forecast_data['main']['temp']} °C")
            print(f"🌡️  Feels like  : {forecast_data['main']['feels_like']} °C")
            print(f"💧 Humidity    : {forecast_data['main']['humidity']}%")
            print(f"☁  Weather     : {forecast_data['weather'][0]['description'].title()}")
            print(f"🌬  Wind Speed  : {forecast_data['wind']['speed']} m/s")
def clear_history():
    search_history.clear()
    print("History Created!")
while True:
    print("=" * 40)
    print("      WEATHER DASHBOARD")
    print("=" * 40)
    try:
        choice = int(input("Enter Choice:\n1)Current Weather\n2)Search History\n3)5-Day Forecast\n4)Clear History\n5)Exit\n"))
        if choice == 1:
            current_weather()
            input("\nPress Enter to Continue....")
            clear_screen()
        elif choice == 2:
            view_history()
            input("\nPress Enter to return to the menu... ")
        elif choice == 3:
            weather_forecast()
        elif choice == 4:
            clear_history()
        elif choice == 5:
            print("Thank you for using Weather Dashboard!")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Please Ente a Number!")
