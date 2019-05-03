import sys
import io
import urllib.request as req
from urllib.parse import urlparse
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8")

# imgURL = "http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg"
# req.urlretrieve(imgURL, savePath1)
# f = req.urlopen(imgURL)
# savePath = "./test.jpg"
# saveFile = open(savePath, "wb")
# saveFile.write(f.read())
# saveFile.close()

# googleURL = "http://google.com"
# req.urlretrieve(googleURL, savePath2)
# f = req.urlopen(googleURL).read()
# savePath = "./test.html"
# with open(savePath, "wb") as saveFile:
#     saveFile.write(f)

# encarURL = "http://www.encar.com"
# mem = req.urlopen(encarURL)
# print("geturl: ", mem.geturl())
# print("status: ", mem.status)
# print("headers: ", mem.getheaders())
# print("info: ", mem.info())
# print("code: ", mem.getcode())
# print("read: ", mem.read(50 ).decode("utf-8"))
# print(urlparse(encarURL))

# API = "https://api.ipify.org"
# values = {
# 	'format': 'json'
# }
# params = urlencode(values)
# url = API + "?" + params
# reqData = req.urlopen(url).read().decode('utf-8')
# print('before: ', values)
# print('after: ', params)
# print("URL: ", url)
# print("data: ", reqData)

# API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
# values = {"ctxCd": "1001"}
# params = urlencode(values)
# url = API + "?" + params
# print("URL: ", url)

print("Complete!")
