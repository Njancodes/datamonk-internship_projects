import sqlite3 
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute("""
                    SELECT DISTINCT cat.name, SUM(COUNT(ren.inventory_id)) OVER(
                    PARTITION BY cat.name) AS rentals_category
                    FROM rental ren
                    JOIN inventory i ON i.inventory_id == ren.inventory_id
                    JOIN film f ON f.film_id == i.film_id
                    JOIN film_category fc ON fc.film_id == f.film_id
                    JOIN category cat ON cat.category_id == fc.category_id
                    GROUP BY ren.inventory_id, cat.name;
               """)

catrentaldata = cursor.fetchall()

category, ren_num = zip(*catrentaldata)

print(category)
print(ren_num)

fig = plt.figure(figsize=(10,7))
plt.title("Category Distribution")
plt.pie(ren_num,labels=category,autopct='%.1f%%',wedgeprops={'linewidth':1.0,'edgecolor':'white'})


plt.savefig("categorybyrentalcount.jpg")
plt.show()

