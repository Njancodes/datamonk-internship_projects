import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute("SELECT strftime('%w',rental_date), COUNT(*) FROM rental GROUP BY strftime('%w',rental_date);")

rentaldate = cursor.fetchall()

day, count = zip(*rentaldate)

dayname = []
idx = 0
for i in day:
    match int(i):
        case 0:
            dayname.append('Sunday')
        case 1:
            dayname.append('Monday')
        case 2:
            dayname.append('Tuesday')
        case 3:
            dayname.append('Wednesday')
        case 4:
            dayname.append('Thursday')
        case 5:
            dayname.append('Friday')
        case 6:
            dayname.append('Saturday')
        case _:
            print('Unknown Day')
    idx+= 1
print(dayname)
print(day)
print(count)

plt.figure(figsize=(10,5))
plt.bar(dayname, count, color='green')
plt.title('Rentals by Day of the Week')
plt.xlabel('Day of the week')
plt.ylabel('Number of rentals')

plt.savefig('rentalsbyday.jpg')
plt.show()

