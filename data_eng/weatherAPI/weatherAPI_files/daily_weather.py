import sqlite3


def insertdailyweather(location_name):

    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    res = cursor.execute("SELECT location_name, date, ROUND(MAX(temp),2),ROUND(MIN(temp),2),ROUND(AVG(humidity),2) FROM weather WHERE location_name = ? GROUP BY location_name, date ;", (location_name,))
    for (ln, date, maxtemp, mintemp, avghum) in res.fetchall():

        print(ln)
        print(date)
        print(maxtemp)
        print(mintemp)
        print(avghum)

        cursor.execute("INSERT INTO daily_weather (location_name, date, max_temp, min_temp, avg_humidity) VALUES (?, ?, ?, ?, ?);", (ln, date, maxtemp, mintemp, avghum))
        conn.commit()

    cursor.close()
    conn.close()

