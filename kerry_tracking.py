from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
import time

##############################################################################################
# 우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음
baseUrl = "https://th.kerryexpress.com/th/track/?track="
plusUrl = "sly2000312465"

# 입력된 송장번호로 검색
url = baseUrl + quote_plus(plusUrl)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_class_name("ke-btn-search").click()

# time.sleep(2)


# #배송정보를 스크랩
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# table = soup.find_all("div", {"class": "d-flex flex-column flex-sm-row flex-fill pl-3"})
# times = soup.find_all("div", {"class":"text-sm-right d-flex flex-column py-2"})

# places = []
# for info in table:
#     places.append(info.find("span", {"class":"header bold"}).text)
#     places.append(info.find("span", {"class": "text-1418 light"}).text)

# dates = []
# for time in times:
#     dates.append(time.find("span", {"class": "text-1418 light"}).text)

# print(places)
# print(dates)
# driver.close()
