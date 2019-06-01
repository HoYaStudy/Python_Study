import os.path
import urllib.request as req
from bs4 import BeautifulSoup

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
fname = "./forecast.xml"

if not os.path.exists(fname):
    req.urlretrieve(url, fname)

xml = open(fname, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, "html.parser")

info = {}
for location in soup.find_all("location"):
    city = location.find("city").string
    weather = location.find_all("tmn")
    if not (city in info):
        info[city] = []
    for tmn in weather:
        info[city].append(tmn.string)

with open("./forecast.txt", "wt") as f:
    for city in sorted(info.keys()):
        f.write(str(city) + "\n")
        for w in info[city]:
            f.write("\t" + str(w))
        f.write("\n")
