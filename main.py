from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import requests
import time

from flask import Flask, render_template, request, redirect
#request는 우리가 입력한 자료를 받아오기 위해서 import하는거야 

db = {}

app = Flask("SuperScrapeer")

@app.route("/")
def home():
    return render_template("home.html")
# @는 데코레이터로 바로 아래에 있는 함수를 찾는데 그 함수를 데코레이트 해주는 역할을 해 

@app.route("/report")
def report():
    word = request.args.get("word")
    
    word = word.lower()
            
    #우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음 
    baseUrl = 'https://th.kerryexpress.com/th/track/?track='
    plusUrl = word

    #입력된 송장번호로 검색 
    url = baseUrl + quote_plus(plusUrl)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.find_element_by_class_name('ke-btn-search').click()
    #WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ke-btn-search')))
    #driver.implicitly_wait(3)
    time.sleep(2)


    #배송정보를 스크랩 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("div", {"class": "d-flex flex-column flex-sm-row flex-fill pl-3"})
    dates = soup.find_all("div", {"class":"text-sm-right d-flex flex-column py-2"})

    places = []
    for info in table:
        places.append(info.find("span", {"class":"header bold"}).text)
        places.append(info.find("span", {"class": "text-1418 light"}).text)            

    arrive_tiem = []
    for date in dates:
        arrive_tiem.append(date.find("span", {"class": "text-1418 light"}).text)
    
    driver.close()

    return render_template("report.html", searchingBy=word, places=places, dates=dates)

app.run(host="127.0.0.1")

