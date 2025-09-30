import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('sakila.db')
cursor = conn.cursor()

cursor.execute("""
                SELECT DISTINCT f.length, SUM(COUNT(ren.inventory_id)) OVER(PARTITION BY f.length) AS total_rental_cnt
                FROM rental AS ren
                JOIN inventory iv ON iv.inventory_id == ren.inventory_id
                JOIN film f ON f.film_id == iv.film_id
                GROUP BY ren.inventory_id;
               """)

lengthcountdata = cursor.fetchall()

length, rental_cnt = zip(*lengthcountdata)

plt.figure(figsize=(10,5))
plt.scatter(length, rental_cnt, color='olive')
plt.title("Film Length vs. Rental Count")
plt.xlabel("Film Length")
plt.ylabel("Rental Count")

plt.savefig('filmlengthvsrentalcount.jpg')
plt.show()

