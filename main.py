from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
from flask import Flask, render_template, request, redirect


db = {}

app = Flask("SuperScrapeer")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    
    word = word.lower()


    #우리가 원하는 사이트를 들어가서 사용자가 송장번호 입력할 수 있음 
    baseUrl = 'https://th.kerryexpress.com/th/track/?track='
    plusUrl = word


    #입력된 송장번호로 검색 
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(options=options)
    url = baseUrl + quote_plus(plusUrl)
    driver.get(url)
    driver.find_element_by_class_name('ke-btn-search').click()
    time.sleep(2)


    #배송정보를 스크랩 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("div", {"class": "d-flex flex-column flex-sm-row flex-fill pl-3"})
    dates = soup.find_all("div", {"class":"text-sm-right d-flex flex-column py-2"})

    titles = []
    for info in table:
        titles.append(info.find("span", {"class":"header bold"}).text)

    places = []
    for info in table:
        places.append(info.find("span", {"class": "text-1418 light"}).text)            

    arrives = []
    for date in dates:
        arrives.append(date.find("span", {"class": "text-1418 light"}).text)
    
    driver.close()

    return render_template("report.html", searchingBy=word, titles=titles, places=places, arrives=arrives)

app.run(host="127.0.0.1")

