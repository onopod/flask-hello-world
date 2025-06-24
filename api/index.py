# usage
# FLASK_APP=api.index.py flask run
# 参考ページ
# https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&cb=0.0&ct=9999999&et=9999999&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&srch_navi=1

from flask import Flask, render_template
from .diary import diary_bp

app = Flask(__name__)
app.register_blueprint(diary_bp, url_prefix="/diary")

items = [
    {
        "id": 1,
        "title": "ＪＲ山手線 秋葉原駅 15階建 築3年",
        "price": "143000",
        "url": "https://fastly.picsum.photos/id/940/300/300.jpg?hmac=9fo8dMC0l9QtPjyCC143w0baGIDuMbaTh5O6KkrjGO8"
    }, 
    {
        "id": 2,
        "title": "パークルール大手町",
        "price": "192000",
        "url": "https://fastly.picsum.photos/id/880/300/300.jpg?hmac=oXC1t0jViOdGm6k__5wE0t1X0riYREqUm9z2CZuIfEI"
    },
    {
        "id": 3,
        "title": "テスト物件",
        "price": "132000",
        "url": "https://fastly.picsum.photos/id/880/300/300.jpg?hmac=oXC1t0jViOdGm6k__5wE0t1X0riYREqUm9z2CZuIfEI"
    }
]

@app.route("/")
def index():
    return "Hello, World!!"

@app.route("/list")
def list():
    return render_template("list.html")

@app.route("/list2")
def list2():
    return render_template("list2.html", items=items)

@app.route("/list3")
def list3():
    return render_template("list3.html", items=items)

@app.route("/detail/<int:id>")
def detail(id):
    item = next((item for item in items if item["id"] == id), None)
    return render_template("detail.html", item=item)