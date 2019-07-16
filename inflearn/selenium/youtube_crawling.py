import time
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from io import BytesIO
import xlsxwriter


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--mute-audio')

# browser = webdriver.Chrome('./chromedriver.exe')
browser = webdriver.Chrome('./chromedriver.exe', options=chrome_options)
browser.implicitly_wait(2)
browser.set_window_size(1920, 1280)
browser.get('https://www.youtube.com/watch?v=oS8f7fbMHbI')
time.sleep(2)
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'html'))).send_keys(Keys.PAGE_DOWN)
time.sleep(2)
# print('Before Page Contents: {}'.format(browser.page_source))
scroll_pause_time = 2
last_height = browser.execute_script('return document.documentElement.scrollHeight')
# last_height = browser.execute_script('return document.body.scrollHeight')		# IE
while True:
    browser.execute_script('window.scrollTo(0, document.documentElement.scrollHeight)')
    time.sleep(scroll_pause_time)
    new_height = browser.execute_script('return document.documentElement.scrollHeight')
    print('Last Height: {}, Current Height: {}'.format(last_height, new_height))
    if new_height == last_height:
        break
    last_height = new_height

workbook = xlsxwriter.Workbook('./result.xlsx')
worksheet = workbook.add_worksheet()
row = 2

soup = BeautifulSoup(browser.page_source, 'html.parser')
top_level = soup.select('div#menu-container yt-formatted-string#text')
comment = soup.select('ytd-comment-renderer#comment')
for dom in comment:
    img_src = dom.select_one('#img').get('src')
    author = dom.select_one('#author-text > span').text.strip()
    content = dom.select_one('#content-text').text.strip()
    vote = dom.select_one('#vote-count-middle').text.strip()
    print('Thumbnail: {}'.format(img_src if img_src else 'None'))
    print('Author: {}'.format(author))
    print('Content: {}'.format(content))
    print('Vote: {}'.format(vote))

    worksheet.write('A%s' % row, author)
    worksheet.write('B%s' % row, content)
    worksheet.write('B%s' % row, vote)
    if img_src:
        img_data = BytesIO(req.urlopen(img_src).read())
        worksheet.insert_image('D%s' % row, author, {'image_data': img_data})
    else:
        worksheet.write('D%s' % row, 'None')
    row += 1

browser.quit()
workbook.close()
