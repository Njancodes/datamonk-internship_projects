import requests
import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("indcit.db");
cursor = conn.cursor();

wmo_codes = {
    0:  "Clear sky",
    1:  "Mainly clear",
    2:  "Partly cloudy",
    3:  "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm (slight or moderate)",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail"
}


'''
    City -> The cities in the indcit.db
    The hourly weather for dates within one month of the current data and 4 days ahead of the current date

'''

def getHourlyFromCity(gcity):

    cityres =  cursor.execute(f"""
        SELECT latitude,longitude
        FROM cities
        WHERE city="{gcity}";
    """)

    cityloc = cityres.fetchone()

    if cityloc == None:
        print(f"There is no city with the name {gcity} in our database.")
        exit(1)


    (lat, long) = cityloc
    #print(lat)
    #print(long)

    res = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m,weather_code,relative_humidity_2m&past_days=31&forecast_days=4")
    
    data = res.json()["hourly"] 

    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "lat": lat,
        "lon": long,
        "format": "json"
    }

    headers = {
        # Nominatim requires a valid identifying User-Agent
        "User-Agent": "MyPythonApp/2.0 (nicholson@gmail.com)"
    }

    locres = requests.get(url, params=params, headers=headers)
    print(locres)
    locdata = locres.json()["address"]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude":lat,
        "longitude":long,
        "timezone":"auto"
    }

    timezoneres = requests.get(url, params=params)
    timezone = timezoneres.json()["timezone"]

    retdata = {
        "date":data["time"],
        "temp": data["temperature_2m"],
        "code": data["weather_code"],
        "humid": data["relative_humidity_2m"],
        "region": locdata["state"] if locdata.get("state", None) is not None else locdata["city_district"],
        "country":locdata["country"],
        "lat":lat,
        "long":long,
        "timezone":timezone
            }

    return retdata

def codeTodesc(wmo):
    return wmo_codes.get(wmo)

    '''
    data = res.json()["hourly"]
    #This is will be an issue if more than one semicolons in date
    fdate = data["time"][0].split(":")[0]
    ldate = data["time"][len(data["time"]) - 1].split(":")[0]
    
    firstdate = datetime.strptime(fdate,"%Y-%m-%dT%H")
    givendate = datetime.strptime(gdate,"%Y-%m-%dT%H")

    if(givendate < firstdate or givendate > (firstdate + timedelta(days=34))):
        raise ValueError(f"The date given should be in the [{fdate}-{ldate}]")

    entry = ((givendate - firstdate).days * 24 ) + 1
    print(entry)
    temp = data["temperature_2m"][entry]
    code = data["weather_code"][entry] 
    desc = wmo_codes.get(code)
    humid = data["relative_humidity_2m"][entry]

    print(f"The date is {gdate}")
    print(f"The temperature is {temp}")
    print(f"The weather is {desc} and its code is {code}")
    print(f"The humidity is {humid}%")
    '''
