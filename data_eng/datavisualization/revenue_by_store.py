import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("sakila.db")
cursor = conn.cursor()

cursor.execute("""
                SELECT st.store_id, SUM(pay.amount)
                FROM payment pay
                JOIN staff sf ON sf.staff_id == pay.staff_id
                JOIN store st ON st.store_id == sf.store_id
                GROUP BY st.store_id;
               """)

revstdata = cursor.fetchall()

name, revenue = zip(*revstdata)

stringname = [str(x) for x in name]

plt.figure(figsize=(10,5))
plt.bar(stringname, revenue, color='red')
plt.title('Store Revenue')
plt.xlabel('Store Name')
plt.ylabel('Revenue')

plt.savefig('revenuebystore.jpg')
plt.show()

