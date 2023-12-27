import requests

URLL= "http://api.openweathermap.org/data/2.5/weather?"
API= open('api.txt', 'r').read()
CITY = 'Saint Petersburg'

def kelv_to_cels(kelvin):
    celsius = kelvin - 273
    return celsius


url = URLL + "appid=" + API + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response ['main']['temp']
temp_celsi = kelv_to_cels(temp_kelvin)
humidity = response['main']['humidity']
pressure = response['main']['pressure']

print(f"Temperature in {CITY}: {temp_celsi:.2f}°С")
print(f"Humidity in {CITY}: {humidity:.2f}%")
print(f"Pressure in {CITY}: {pressure:.2f}Pa")
