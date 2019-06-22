import datetime
import pymysql
import simplejson as json

# Print information
print("pymysql.version:", pymysql.__version__)

# Create Datetime
now = datetime.datetime.now()
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")

# Connect to DB
conn = pymysql.connect(
    host="localhost", user="hoya", password="1234", db="mysql_db1", charset="utf8"
)

# Select DB
# conn.select_db('mysql_db1')

# Connect to Cursor
# c = conn.cursor()

# Create DB
# c.execute("CREATE DATABASE mysql_db2")

# Create Table
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, username varchar(20), email varchar(30), phone varchar(30), website varchar(30), regdate varchar(20) NOT NULL, PRIMARY KEY(id))"
)

try:
    with conn.cursor() as c:
        with open("./user.json", "r") as f:
            r = json.load(f)
            userData = []
            for user in r:
                t = (
                    user["id"],
                    user["username"],
                    user["email"],
                    user["phone"],
                    user["website"],
                    nowDateTime,
                )
                userData.append(t)
            c.executemany(
                "INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s, %s)",
                userData,
            )
        conn.commit()
finally:
    conn.close()

# Print Table
try:
    with conn.cursor() as c:
        # with conn.cursor(pymysql.cursors.DictCursor) as c:
        c.execute("SELECT * FROM users")
        print(c.fetchone())
        print(c.fetchmany(3))
        print(c.fetchall())

        rows = c.fetchall()
        c.execute("SELECT * FROM users ORDER BY id ASC")
        for row in rows:
            print("usage 1 >", row)

        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print("usage 2 >", row)

        param1 = (1,)
        c.execute("SELECT * FROM users WHERE id=%s", param1)
        print("param1:", c.fetchall())

        param2 = 1
        c.execute("SELECT * FROM users WHERE id='%d'" % param2)
        print("param2:", c.fetchall())

        param3 = (4, 5)
        c.execute("SELECT * FROM users WHERE id IN(%s, %s)", param3)
        print("param3:", c.fetchall())

        c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (4, 5))
        print("param4:", c.fetchall())
finally:
    conn.close()

# Update and Delete Data
try:
    with conn.cursor() as c:
        c.execute('UPDATE users SET username=%s WHERE id=%s', ('niceman', 1))
        c.execute('UPDATE users SET username='%s' WHERE id='%d'', ('goodgirl', 2))

        c.execute('SELECT * FROM users ORDER BY id DESC')
        for row in c.fetchall():
            print('check 1 >', row)

        c.execute('DELETE FFROM users WHERE id=%s', (1, ))
        c.execute('DELETE FFROM users WHERE id='%s'' % (2, ))
    conn.commit()
finally:
    conn.close()

# Close DB
# c.close()
# conn.close()

# Transaction
# conn.begin()
# conn.commit()
# conn.rollback()
