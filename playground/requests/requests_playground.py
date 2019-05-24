import json
import requests

# url = "http://httpbin.org/get"
# headers = {"user-agent": "HoYa"}
# with requests.Session() as s:
#     r = s.get(url, headers=headers)
#     print(r.text)
#     print(r.status_code)

# url = "https://jsonplaceholder.typicode.com/posts/1"
# with requests.Session() as s:
#     r = s.get(url)
#     print(r.json())
#     print(r.json().keys())
#     print(r.json().values())
#     print(r.encoding)
#     print(r.content)

url = "http://httpbin.org/stream/20"
with requests.Session() as s:
    r = s.get(url, stream=True)
    if r.encoding is None:
        r.encoding = "utf-8"

    for line in r.iter_lines(decode_unicode=True):
        l = json.loads(line)
        for k in l.keys():
            print("key: ", k, ", values: ", l[k])
