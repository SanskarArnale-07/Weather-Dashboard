from datetime import datetime
import requests
url = "https://api.openweathermap.org/data/2.5/weather"
def current_weather():
    city = input("Enter the City: ")
    params = {
        "q" : city,
        "appid" : "33dced3bffa73140df2617cf05bc0b8a" ,
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


print("=" * 40)
print("      WEATHER DASHBOARD")
print("=" * 40)
try:
    choice = int(input("Enter Choice:\n1)Current Weather\n2)Exit\n"))
    if choice == 1:
        current_weather()
    elif choice == 2:
        pass
except ValueError:
    print("Please Enter the Correct Choice!")
