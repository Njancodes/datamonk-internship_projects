import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("SELECT condition,COUNT(condition) FROM weather WHERE location_name = 'Chennai' AND date >= '2025-09-01' AND date < '2025-10-01' GROUP BY condition;")

data = cursor.fetchall()
desc, no_of_condition = zip(*data)

plt.figure(figsize=(10,7))
plt.title("Overall weather condition distribution for Chennai this month")
plt.pie(no_of_condition,labels=desc)

plt.savefig("4_chennai_weather_condition_distribution.png")
plt.show()



