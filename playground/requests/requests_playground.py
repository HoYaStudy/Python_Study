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

# url = "http://httpbin.org/stream/20"
# with requests.Session() as s:
#     r = s.get(url, stream=True)
#     if r.encoding is None:
#         r.encoding = "utf-8"

#     for line in r.iter_lines(decode_unicode=True):
#         l = json.loads(line)
#         for k in l.keys():
#             print("key: ", k, ", values: ", l[k])

# url = "https://api.github.com/events"
# r = requests.get(url)
# r.raise_for_status()

# jar = requests.cookies.RequestsCookieJar()
# jar.set("name", "kim", domain="httpbin.org", path="/cookies")
# r = requests.get("http://httpbin.org/cookies", cookies=jar)
# r.raise_for_status()
# print(r.text)

# r = requests.get("https://github.com", timeout=3)
# print(r.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set("age", "18", domain="httpbin.org", path="/cookies")
# r = requests.post("http://httpbin.org/post", data={"name": "kim"}, cookies=jar)
# print(r.text)

# payload1 = {"key1": "value1", "key2": "value2"}
# payload2 = (("key1", "value1"), ("key2", "value2"))
# payload3 = {"key1": "value1"}
# r = requests.post("http://httpbin.org/post", data=payload1)
# r = requests.post("http://httpbin.org/post", data=payload2)
# r = requests.post("http://httpbin.org/post", data=json.dumps(payload3))
# r = requests.put("http://httpbin.org/put", data=payload1)
# r = requests.delete("http://httpbin.org/delete")
# r = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=payload1)
# r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print(r.text)
