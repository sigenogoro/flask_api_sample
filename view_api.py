
from flask import Flask, jsonify, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime
import requests

app = Flask(__name__)

#簡易DB
array_remind = [
    # {'title':"hoge", "content": "hoge", "day": "2019-08-28"},
]


@app.route("/api/index")
def schedule_index():
    return jsonify(array_remind)

@app.route("/api/create", methods=["POST"])
def create():
    if request.method == "POST":
        data = {
            "title": request.args.get("title",""),
            "content": request.args.get("context",""),
            "day": request.args.get("day","")
        }
        data_s = db_remind(data)
        return '', 204


@app.route("/api/detail", methods=["GET"])
def detail():
    return jsonify(request.form)


def db_remind(dict_params):
    array_remind.append(dict_params)
    return array_remind



if __name__ in "__main__":
    app.run(debug=True, threaded=True, port=3000)