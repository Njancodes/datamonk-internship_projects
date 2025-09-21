from hourly_weather import insertHourlyData
from daily_weather import insertdailyweather
from global_weather import insertglobalweather
import sqlite3

city = input("Which city in india do you want: ").strip().capitalize();
print("Chosen city: ",city)

def create_table():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    isweather = cursor.execute("SELECT COUNT(name) FROM sqlite_master WHERE name = 'weather';").fetchone()[0]
    isdailyweather = cursor.execute("SELECT COUNT(name) FROM sqlite_master WHERE name = 'daily_weather';").fetchone()[0]
    isglobalweather = cursor.execute("SELECT COUNT(name) FROM sqlite_master WHERE name = 'global_weather';").fetchone()[0]
    
    if isweather != 1:
        print("weather table is not present in the database")
        cursor.execute("CREATE TABLE weather (date DATE, time TIME, temp REAL, condition TEXT, humidity REAL, location_name TEXT, region TEXT, country TEXT, lat REAL, long REAL, local_time DATETIME);")
        print("Created the weather table")
    else:
        print("weather table is present in the database")
        known_cities_res = cursor.execute("SELECT DISTINCT location_name FROM weather;")
        if (city,) in known_cities_res.fetchall():
            print("This city's weather data is aldready present.")
            exit(1)
        else:
            print("This city's weather data is not present.")
        
    if isdailyweather != 1:
        print("daily weather table is not present in the database")
        cursor.execute("CREATE TABLE daily_weather (location_name TEXT, date DATE, max_temp REAL, min_temp REAL, avg_humidity REAL);")
        print("Created the daily weather table")
    else:
        print("daily weather table is present in the database")
    if isglobalweather != 1:
        print("global weather table is not present in the database")
        cursor.execute("CREATE TABLE global_weather (location_name TEXT, max_temp REAL, min_temp REAL, avg_humidity REAL);")
        print("Created the global weather table")
    else:
        print("global weather table is present in the database")
    
    cursor.close()
    conn.close()

create_table()
insertHourlyData(city)
insertdailyweather(city)
insertglobalweather(city)
