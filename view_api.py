
from flask import Flask, jsonify, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime

app = Flask(__name__)

array_remind = {'title':[], 'content':[],'day':[]}


@app.route("/api/index")
def schedule_index():
    month_current = Calendar().monthdatescalendar(2019, 8)
    return jsonify(month_current)

@app.route("/api/create", methods=["POST"])
def create():
    pass


@app.route("/api/detail", methods=["GET"])
def detail():
    return jsonify(request.form)




def db_remind(title, content, day):
    array_remind['title'].append(title)
    array_remind['content'].append(content)
    array_remind['day'].append(day)
    return array_remind







if __name__ in "__main__":
    app.run(debug=True, threaded=True, port=3000, host="localhost")