import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('data.db')
cursor = conn.cursor()


cursor.execute("SELECT location_name, ROUND(AVG(avg_humidity),2) as ah FROM daily_weather WHERE (date >= '2025-09-14' AND date < '2025-09-21') GROUP BY location_name ORDER BY ah DESC LIMIT 4");

data = cursor.fetchall()
cities, avg_humidity = zip(*data)

plt.figure(figsize = (10,6))
plt.barh(cities[::-1],avg_humidity[::-1],color='skyblue')
plt.title("Top 4 Highest Humid cities last week")
plt.xlabel("Average Humidity over last week")
plt.ylabel("Cities")
plt.grid(True)

plt.savefig("2_4_highest_humid_cities_last_week.png")

plt.show()
