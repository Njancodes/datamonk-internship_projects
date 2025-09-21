import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("SELECT date, max_temp, min_temp FROM daily_weather WHERE location_name = 'Jaipur' ORDER BY date DESC LIMIT 3");

rows = cursor.fetchall();
dates, max_temp, min_temp = zip(*rows)

plt.figure(figsize=(10,5))
plt.plot(dates, max_temp,marker='o',label='Max Temp',color='orange')
plt.plot(dates, min_temp,marker='x', label='Min Temp',color='blue')
plt.title("Jaipur Temperature Trend - Last 3 Days")
plt.xlabel("Date")
plt.ylabel("Temperature (*C)")
plt.grid(True)

plt.savefig("3_daytime_and_nighttime_temperatures_of_jaipur.png")

plt.show()
