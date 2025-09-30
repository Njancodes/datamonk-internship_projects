import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute(""" 
                SELECT CONCAT(cst.first_name , ' ', cst.last_name), COUNT(*)
                FROM rental
                JOIN customer cst ON cst.customer_id = rental.customer_id
                GROUP BY rental.customer_id
                ORDER BY COUNT(*)
                DESC LIMIT 5;
               """)

data = cursor.fetchall()

names, ren_num = zip(*data)

plt.figure(figsize=(10,5))
plt.bar(names, ren_num, color='purple')
plt.title('Top 5 Customers by Rentals')
plt.xlabel('Customer')
plt.ylabel('Number of rentals')

plt.savefig('top5customerbyrental.jpg')
plt.show()

