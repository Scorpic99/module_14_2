import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

cursor.execute("UPDATE Users SET balance = balance / ? WHERE id % 2 != 0", (2,))

cursor.execute("DELETE FROM Users WHERE id == 1 OR (id - 1) % 3 == 0")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60 GROUP BY username, email, age, balance")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("DELETE FROM Users WHERE id == 6")

cursor.execute("SELECT COUNT(*) FROM Users")
count = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
avg = cursor.fetchone()[0]
print(avg/count)

connection.commit()
cursor.close()