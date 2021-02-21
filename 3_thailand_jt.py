
import time
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


baseUrl = "https://www.jtexpress.co.th/index/query/gzquery.html"
driver = webdriver.Chrome()
driver.get(baseUrl)
elem = driver.find_element_by_id("billcode_list")
elem.send_keys("860091756871")
driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div[2]/div[1]/button").click()

time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
table = soup.find_all("div", {"class": "bill_state_item"})

for place in table:
    place = place.find("div", {"class": "bill_state_text"}).get_text()
    print(place)

for date in table:
    date = date.find("div", {"class": "bill_state_day"}).get_text()
    print(date)

driver.close()