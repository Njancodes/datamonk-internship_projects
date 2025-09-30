import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute("SELECT inventory_id, COUNT(inventory_id) as noofrentals FROM rental GROUP BY inventory_id ORDER BY noofrentals DESC LIMIT 10;")

idnumber = cursor.fetchall()
invids, numberrentals = zip(*idnumber)
filmtitles = {}

for i in range(0,len(invids)):
    cursor.execute("SELECT film_id FROM inventory WHERE inventory_id = ?",(invids[i],))
    filmid = cursor.fetchone()[0]
    cursor.execute("SELECT title FROM film WHERE film_id = ?",(filmid,))
    filmtitles[cursor.fetchone()[0]] = numberrentals[i]

plt.figure(figsize=(10,10))
plt.bar(filmtitles.keys(), filmtitles.values(), color='blue')
plt.xticks(rotation=20)
plt.title("10 Most Popular Films")
plt.xlabel("Movies")
plt.ylabel("Number Of Rentals")
plt.grid(True)

plt.savefig("10mostpopularfilms.jpg")
plt.show()

