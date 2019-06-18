import simplejson as json
from tinydb import TinyDB, Query, where
from tinydb.storages import MemoryStorage

# Create DB (File)
db = TinyDB("./tinydb.db", default_table="users")

# Create DB (Memory)
# db = TinyDB(storage=MemoryStorage, default_table="users")

# Select Table
users = db.table("users")
todos = db.table("todos")
tests = db.table("tests")

# Insert Data to Table
# users.insert({"name": "kim", "email": "kim@google.com"})
# todos.insert({"item": "homework", "complete": False})
tests.insert_multiple(
    [
        {"name": "kim", "email": "kim@google.com"},
        {"name": "lee", "email": "lee@google.com"},
        {"name": "park", "email": "park@google.com"},
    ]
)

# Insert Json Data to Table
with open("./users.json", "r") as f:
    r = json.loads(f.read())
    for u in r:
        users.insert(u)
with open("./todos.json", "r") as f:
    r = json.loads(f.read())
    for t in r:
        todos.insert(t)

# Print Table
# print(db.all())
# print(db.tables())
# print(users.all())
# print(todos.all())
# for u in users:
#     print(u['username'], ': ', u['phone'])
# for t in todos:
#     print(t['title'], ': ', t['completed'])

# Join
# for u in users:
#     print("[", u["username"], "]")
#     for t in todos:
#         if t["userId"] == u["id"]:
#             print(t["title"])

# Query
Users = Query()
Todos = Query()
Test = Query()
# users.update({"username": "kim"}, Users.id == 3)
# print(users.search(Users.id == 3))
# print(users.search(Users["id"] == 3))
# print(users.search(where("id") == 3))
# print(users.search(Query()["id"] == 3))
# users.remove(Users.id == 3)
# print(users.search(Users.id == 3))
# print(users.search(where("address")["zipcode"] == "90566-7771"))
# print(users.search(where("address").zipcode == "90566-7771"))
# print(users.search(Users.email.exists()))
# print(users.search(Users.aaa.exists()))  # No exist
# print("NOT:", users.search(~(Users.username == "Antonette")))
# print(
#     "OR:", users.search((Users.username == "Antonette") | (Users.username == "Kamren"))
# )
# print("AND:", users.search((Users.username == "Antonette") & (Users.id == 2)))
# print("LEN:", len(users), ",", len(todos))
# print("CONTAINS:", users.contains(Users.username == "Kamren"))
# print("COUNT:", users.count(Users.username == "Kamren"))
# print(users.get(Users.id == 5))
# print(users.get(Users.id == 5).doc_id)
# print(tests.update({"email": "test@google.com"}, doc_ids=[1, 3]))
# print(tests.update({"email": "test@naver.com"}, Test.name == "park"))

# Delete Data in Table
users.purge()
todos.purge()
# db.purge_table("users")
# db.purge_table("todos")
tests.remove(doc_ids=[1, 3])
tests.remove(Test.name == "park")

# Delete Table
db.purge_tables()

# Close DB
db.close()
