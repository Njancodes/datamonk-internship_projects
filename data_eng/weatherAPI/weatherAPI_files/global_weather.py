import sqlite3


def insertglobalweather(location_name):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    res = cursor.execute("SELECT location_name, ROUND(AVG(max_temp), 2), ROUND(AVG(min_temp), 2), ROUND(AVG(avg_humidity), 2) FROM daily_weather WHERE location_name = ? GROUP BY location_name ;",(location_name,))

    (ln, avgmaxtemp, avgmintemp, avghumidity) = res.fetchone();

    cursor.execute("INSERT INTO global_weather (location_name, max_temp, min_temp, avg_humidity) VALUES (?,?,?,?);", (ln,avgmaxtemp,avgmintemp, avghumidity))
    conn.commit()

    cursor.close()
    conn.close()
