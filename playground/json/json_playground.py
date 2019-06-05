import os.path
import urllib.request as req
import simplejson as json

data = {}
data["people"] = []
data["people"].append(
    {"name": "Kim", "website": "google.com", "city": "Seoul", "grade": [95, 77, 89, 91]}
)
data["people"].append(
    {
        "name": "Lee",
        "website": "google.com",
        "city": "Busan",
        "grade": [85, 67, 100, 93],
    }
)
data["people"].append(
    {
        "name": "Park",
        "website": "google.com",
        "city": "Incheon",
        "grade": [98, 79, 99, 92],
    }
)

d = json.dumps(data, indent=4)
l = json.loads(d)

with open("./member.json", "w") as f:
    f.write(d)

with open("./member.json", "r") as f:
    r = json.loads(f.read())
    for p in r["people"]:
        print("Name:", p["name"])
        print("Website:", p["website"])
        print("City:", p["city"])
        print("")

with open("./member.json", "w") as f:
    json.dump(data, f)

with open("./member.json", "r") as f:
    r = json.load(f)
    for p in r["people"]:
        print("Name:", p["name"])
        print("Website:", p["website"])
        print("City:", p["city"])
        grade = ""
        for g in p["grade"]:
            grade = grade + " " + str(g)
        print("grade:", grade.lstrip())
        print("")

url = "https://api.github.com/repositories"
fname = "./repo.json"
if not os.path.exists(url):
    req.urlretrieve(url, fname)

# items = json.loads(open(fname, 'r', encoding='utf-8').read())
items = json.load(open(fname, "r", encoding="utf-8"))
for item in items:
    print(item["full_name"] + " : " + item["owner"]["url"])
