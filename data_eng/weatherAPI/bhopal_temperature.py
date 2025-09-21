import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


cursor.execute("SELECT date, max_temp, min_temp FROM daily_weather WHERE location_name = 'Bhopal' ORDER BY date DESC LIMIT 5;")

rows = cursor.fetchall()
dates, max_temp, min_temp = zip(*rows[::-1])

plt.figure(figsize=(10,5))
plt.plot(dates,max_temp,marker='o',label='Max Temp',color='red')
plt.plot(dates,min_temp,marker='x',label='Min Temp',color='blue')
plt.title("Bhopal Temperature Trend - Last 5 Days")
plt.xlabel("Date")
plt.ylabel("Temperature (*C)")
plt.legend()
plt.grid(True)
plt.savefig('1_bhopal_temperature_trend_over_last_5_days.png')
plt.show()

