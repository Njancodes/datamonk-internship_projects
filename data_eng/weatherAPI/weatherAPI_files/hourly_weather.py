from weather_utils import getHourlyFromCity, codeTodesc
import sqlite3
from zoneinfo import ZoneInfo
from datetime import datetime

def insertHourlyData(location_name):

    datatemp = getHourlyFromCity(location_name)
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    for i in range(0, len(datatemp["date"])):

        date = datatemp["date"][i].split("T")[0]
        time = datatemp["date"][i].split("T")[1]
        temp = datatemp["temp"][i]
        condition = codeTodesc(datatemp["code"][i])
        humidity = datatemp["humid"][i]
        region = datatemp["region"]
        country=datatemp["country"]
        lat = datatemp["lat"]
        long = datatemp["long"]
        timezone = datatemp["timezone"]
        
        utc_time = datetime.fromisoformat(date+"T"+time).replace(tzinfo=ZoneInfo("UTC"))
        local_time = utc_time.astimezone(ZoneInfo(timezone))

        print(f"This is for the record {i} -------------------")
        print(date)
        print(time)
        print(temp)
        print(condition)
        print(humidity)
        print(location_name)
        print(lat)
        print(long)
        print(local_time)
        print("-----------------------------------------------")
        
        cursor.execute(f"INSERT INTO weather (date, time, temp, condition, humidity, location_name, region, country, lat, long, local_time) VALUES (?,?,?,?,?,?,?,?,?,?,?);", (date, time,temp, condition, humidity, location_name,region,country,lat,long, local_time))
        conn.commit()
        print("Inserted the hourly data successfully")

    cursor.close()
    conn.close()
