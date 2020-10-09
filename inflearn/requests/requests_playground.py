import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# Ruliweb Login ---------------------------------------------------------------#
# LOGIN_INFO = {"user_id": "", "user_pw": ""}
# url = "https://user.ruliweb.com/member/login_proc"
# with requests.Session() as s:
#     login_req = s.post(url, data=LOGIN_INFO)
#     if login_req.status_code == 200 and login_req.ok:
#         post_one = s.get("https://bbs.ruliweb.com/market/board/320102/read/117048?")
#         post_one.raise_for_status()
#         soup = BeautifulSoup(post_one.text, "html.parser")
#         article = soup.select_one("div.view_content").find_all("p")
#         for i in article:
#             if i.string is not None:
#                 print(i.string)
# -----------------------------------------------------------------------------#

# Inflearn Login --------------------------------------------------------------#
# LOGIN_INFO = {"email": "", "password": ""}
# url = "https://www.inflearn.com/api/signin"
# with requests.Session() as s:
#     login_req = s.post(url, data=LOGIN_INFO)
#     if login_req.status_code == 200 and login_req.ok:
#         dash_info = s.get("https://www.inflearn.com/users/35657/dashboard")
#         dash_info.raise_for_status()
#         soup = BeautifulSoup(dash_info.text, "html.parser")
#         statistics = soup.select("div.box.statistics > div.box_content > div > div")
#         for v in statistics:
#             lable = v.find("div", class_="status_label").text.strip()
#             status = v.find("div", class_="status_value").text.strip()
#             print("{} : {}".format(lable, status))
# -----------------------------------------------------------------------------#

# Wishket Login ---------------------------------------------------------------#
# url = "https://www.wishket.com/accounts/login"
# ua = UserAgent()
# with requests.Session() as s:
#     s.get(url)
#     LOGIN_INFO = {
#         "identification": "",
#         "password": "",
#         "csrfmiddlewaretoken": s.cookies["csrftoken"],
#     }
#     rsp = s.post(
#         url,
#         data=LOGIN_INFO,
#         headers={
#             "User-Agent": str(ua.chrome),
#             "Referer": "https://www.wishket.com/accounts/login/",
#         },
#     )
#     if rsp.status_code == 200 and rsp.ok:
#         soup = BeautifulSoup(rsp.text, "html.parser")
#         project_list = soup.select("table.table-responsive > tbody > tr")
#         for i in project_list:
#             print(i.find("th").string, i.find("td").text)
# -----------------------------------------------------------------------------#
