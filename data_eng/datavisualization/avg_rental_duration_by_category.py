import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute("""
                SELECT cat.name, AVG(julianday(strftime('%Y-%m-%d', return_date))- julianday(strftime('%Y-%m-%d',rental_date))) FROM rental
                JOIN inventory iv ON iv.inventory_id == rental.inventory_id
                JOIN film f ON f.film_id == iv.film_id
                JOIN film_category fc ON fc.film_id == f.film_id
                JOIN category cat ON cat.category_id == fc.category_id
                GROUP BY cat.name;
               """)

categorydata = cursor.fetchall()
category, period = zip(*categorydata)

plt.figure(figsize=(10,8))
plt.bar(category, period, color='gray')
plt.title('Average Rental Duration by Category')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.ylabel('Average Rental Duration')

plt.savefig("avgrentaldurationbycategory.jpg")
plt.show()
