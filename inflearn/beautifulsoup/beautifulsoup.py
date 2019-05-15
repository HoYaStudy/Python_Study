import os
import errno
import json
import urllib.request as req
import urllib.parse as parse
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# from DAUM ###################################################################
# ua = UserAgent()
# headers = {"User-Agent": ua.ie, "referer": "https://finance.daum.net"}
# daum_url = "https://finance.daum.net/api/search/ranks?limit=10"
# rsp = req.urlopen(req.Request(daum_url, headers=headers)).read().decode("utf-8")

# rank = json.loads(rsp)["data"]
# for elem in rank:
#     print(elem["rank"], elem["name"], elem["tradePrice"])
###############################################################################

# from NAVER (Finance) ########################################################
# naver_url = "https://finance.naver.com/sise"
# rsp = req.urlopen(naver_url).read()
# soup = BeautifulSoup(rsp, "html.parser")

# top10 = soup.select("#siselist_tab_0 > tr")
# index = 1
# for i in top10:
#     if i.find("a") is not None:
#         print(index, i.select_one(".tltle").string)
#         index += 1
###############################################################################

# from NAVER (Image) ##########################################################
# base_url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
# quote = parse.quote_plus("범고래")
# url = base_url + quote
# rsp = req.urlopen(url).read()
# soup = BeautifulSoup(rsp, "html.parser")

# save_path = "./image/"
# try:
#     if not (os.path.isdir(save_path)):
#         os.makedirs(os.path.join(save_path))
# except OSError as e:
#     if e.errno != errno.EEXIST:
#         print("Error: Fail to make directory")
#         raise

# img_list = soup.select("div.img_area > a.thumb._thumb > img")
# for i, img_list in enumerate(img_list, 1):
#     fname = os.path.join(save_path, str(i) + '.jpg')
#     req.urlretrieve(img_list["data-source"], fname)
###############################################################################
