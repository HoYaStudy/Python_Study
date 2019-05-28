import time
from selenium import webdriver

# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

# Chrome ---------------------------------------------------------------------#
# driver = webdriver.Chrome("./selenium/chromedriver")
# driver.set_window_size(1920, 1080)
# driver.get("https://google.com")
# time.sleep(5)
# driver.save_screenshot("./selenium/google.png")
# driver.get("https://www.daum.net")
# time.sleep(5)
# driver.save_screenshot("./selenium/daum.png")
# driver.quit()
# print("Complete Screenshot")

# chrome_opt = Options()
# chrome_opt.add_argument("--headless")  # CLI
# driver = webdriver.Chrome(
#     chrome_options=chrome_opt, executable_path=r"./selenium/chromedriver"
# )
# driver.get("https://google.com")
# driver.save_screenshot("./selenium/google.png")
# driver.get("https://www.daum.net")
# driver.save_screenshot("./selenium/daum.png")
# driver.quit()
# print("Complete Screenshot")
# ----------------------------------------------------------------------------#

# FireFox --------------------------------------------------------------------#
firefox_opt = Options()
firefox_opt.add_argument("--headless")  # CLI
driver = webdriver.Firefox(
    firefox_options=firefox_opt, executable_path="./selenium/geckodriver"
)
driver.get("https://google.com")
driver.save_screenshot("./selenium/google.png")
driver.get("https://www.daum.net")
driver.save_screenshot("./selenium/daum.png")
driver.quit()
print("Complete Screenshot")
# ----------------------------------------------------------------------------#

# PhantomJS ------------------------------------------------------------------#
# driver = webdriver.PhantomJS("./selenium/phantomjs")
# driver.implicitly_wait(5)
# driver.get("https://google.com")
# driver.save_screenshot("./selenium/google.png")
# driver.implicitly_wait(5)
# driver.get("https://www.daum.net")
# driver.save_screenshot("./selenium/daum.png")
# driver.quit()
# print("Complete Screenshot")
# ----------------------------------------------------------------------------#

