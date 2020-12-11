from flask import Flask, render_template, escape, request

app = Flask(__name__)

 
@app.route("/")
def home():
    return "Hello! this is the main page"
    # return render_template("home.html") 

# @는 데코레이터로 바로 아래에 있는 함수를 찾는데 그 함수를 데코레이트 해주는 역할을 해 

@app.route("/report")
def report():
    print(request.args.get("word"))
    return "This is a text page"

if __name__ == "__main__":
    app.run()
    sdfsdfsdf
    