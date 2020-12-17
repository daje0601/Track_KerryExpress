from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

baseUrl = "https://track.thailandpost.co.th/?lang=en"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
driver = webdriver.Chrome()
driver.get(baseUrl)
elem = driver.find_element_by_class_name("input-track")
# elem.send_keys("ED384490065TH")
# elem.send_keys(Keys.RETURN)

# time.sleep(2)