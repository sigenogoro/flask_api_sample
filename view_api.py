
from flask import Flask, jsonify, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime
import requests

app = Flask(__name__)

#簡易DB
array_remind = []


@app.route("/api/index")
def schedule_index():
    return jsonify(array_remind)

@app.route("/api/create", methods=["POST"])
def create():
    if request.method == "POST":
        data = {
            "title": request.args.get("title",""),
            "context": request.args.get("context",""),
            "day": request.args.get("day","")
        }
        db_remind(data)
        return '', 204

@app.route("/api/edit", methods=["PUT"])
def edit():
    if request.method == "PUT":
        data = {
            "title": request.args.get("title",""),
            "context": request.args.get("context",""),
            "day": request.args.get("day","")
        }
        db_remind(data)
        return '', 204


@app.route("/api/delete", methods=["DELETE"])
def delete():
    if request.method == "DELETE":
        array_remind.clear()
        return '', 204


def db_remind(dict_params):
    if request.method == "POST":
        array_remind.append(dict_params)
        return array_remind
    elif request.method == "PUT":
        for params in array_remind:
            if params['day'] == dict_params['day']:
                params['title'] = dict_params['title']
                params['context'] = dict_params['context']
                return array_remind




if __name__ in "__main__":
    app.run(debug=True, threaded=True, port=3000)