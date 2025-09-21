import sqlite3



def createTables(dbname):
    conn = sqlite3.connect(dbname + ".db") #Create or connect to an aldready existing file
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS weather (date DATE, time TIME, temp REAL, condition TEXT, humidity REAL, location_name TEXT, region TEXT, country TEXT, lat REAL, long REAL, local_time DATETIME);")
    cursor.execute("CREATE TABLE IF NOT EXISTS daily_weather (location_name TEXT, date DATE , maxtemp REAL, mintemp REAL, avghumidity REAL);")
    cursor.execute("CREATE TABLE IF NOT EXISTS global_weather (location_name TEXT, max_temp, min_temp, avg_humidity);")

createTables("mumbai")
