import datetime
import sqlite3
import simplejson as json

# Print Info
print("Version:", sqlite3.version, sqlite3.sqlite_version)

# Create DB
conn = sqlite3.connect("./sqlite3.db")
# conn = sqlite3.connect(':memory:')

now = datetime.datetime.now()
nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Connect Cursor
c = conn.cursor()
print(c)

# Create Table
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, username text, email text, phone text, website text, regdate text)"
)

# Insert Data to Table
# c.execute("INSERT INTO users VALUES (1 ,'kim','kim@naver.com', '010-0000-0000', 'kim.com', ?)", (nowDatetime,))
# userList = (
#     (2, "lee", "lee@naver.com", "010-1111-1111", "lee.com", nowDatetime),
#     (3, "park", "park@naver.com", "010-1111-1111", "park.com", nowDatetime),
#     (4, "choi", "choi@naver.com", "010-1111-1111", "choi.com", nowDatetime),
# )
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

with open("./users.json", "r") as f:
    d = json.load(f)
    userData = []
    for user in d:
        t = (
            user["id"],
            user["username"],
            user["email"],
            user["phone"],
            user["website"],
            nowDatetime,
        )
        userData.append(t)
    c.executemany(
        "INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
        userData,
    )

# Update DB
c.execute("UPDATE users SET username=? WHERE id=?", ("niceman", 1))
c.execute("UPDATE users SET username=:name WHERE id=:id", {"name": "goodgirl", "id": 2})
c.execute("UPDATE users SET username='%s' WHERE id='%s'" % ("handsomeguy", 3))

conn.commit()

# Print DB
# c.execute("SELECT * FROM users")
# print(c.fetchone())
# print(c.fetchmany(size=4))
# print(c.fetchall())

# c.execute("SELECT * FROM users")
# rows = c.fetchall()
# for row in rows:
#     print("usage1 > ", row)

# c.execute("SELECT * FROM users")
# for row in c.fetchall():
#     print("usage2 > ", row)

# for row in c.execute("SELECT * FROM users"):
#     print("usage3 > ", row)

param1 = (1,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print(c.fetchall())
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print(c.fetchall())
c.execute("SELECT * FROM users WHERE id=:id", {"id": "1"})
print(c.fetchall())
param4 = (1, 4)
c.execute("SELECT * FROM users WHERE id IN(?, ?)", param4)
print(c.fetchall())

# Dump
with conn:
    with open("./db.dump", "w") as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("Dump Write Complete!")

# Delete Data in Table
print("Delete users DB", conn.execute("DELETE FROM users").rowcount, "rows")
c.execute("DELETE FROM users WHERE id=?", (4,))

# Commit DB
conn.commit()

# Close DB
conn.close()
