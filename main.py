from flask import Flask, render_template, request
#request는 우리가 입력한 자료를 받아오기 위해서 import하는거야 

app = Flask("SuperScrapeer")

@app.route("/")
def home():
    return render_template("home.html")
# @는 데코레이터로 바로 아래에 있는 함수를 찾는데 그 함수를 데코레이트 해주는 역할을 해 
@app.route("/report")
def report():
    word = request.args.get("word")
    return render_template("report.html", searchingBy=word)

app.run(host="127.0.0.1")

