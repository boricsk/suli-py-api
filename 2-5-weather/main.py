#https://openweathermap.org/
import requests
from pprint import pprint

API_KEY = ''
CURRENT_URL = 'https://api.openweathermap.org/data/2.5/weather'
FORECAST_URL = 'https://api.openweathermap.org/data/2.5/forecast'
GEOCODING_URL = 'http://api.openweathermap.org/geo/1.0/direct'
UNITS = 'metric'
LANG = 'HU'

def getCoordinates(city):
    geocodingPayload = {'q':city,'appid':API_KEY}
    respGeocoding = requests.get(GEOCODING_URL, params=geocodingPayload)
    respGeocoding = respGeocoding.json()[0]
    return respGeocoding['lat'], respGeocoding['lon']

def getForecast(lat, lon):
    forecastPayload = {'lat':lat, 'lon':lon, 'appid':API_KEY, 'units':UNITS, 'lang':LANG}
    respForecast = requests.get(FORECAST_URL, params=forecastPayload)
    respForecast = respForecast.json()
    return respForecast

def getCurrent(lat, lon):
    currentPayload = {'lat':lat, 'lon':lon, 'appid':API_KEY, 'units':UNITS, 'lang':LANG}
    respCurrent = requests.get(CURRENT_URL, params=currentPayload)
    respCurrent = respCurrent.json()
    return respCurrent

def main():
    city = 'Jászapáti'
    cityCoord = getCoordinates(city)
    pprint(getCurrent(cityCoord[0], cityCoord[1]))

main()
'''
Timestamp konverzió
datetime.fromtimestamp(...).strftime(...)

Az strftime paraméter lehet:
'%Y-%m-%d %H:%M:%S' Ez variálható.
'''
