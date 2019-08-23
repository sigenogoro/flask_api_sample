from flask import Flask, jsonify, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime
import requests
app = Flask(__name__)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/")
def index():
    month_current = datetime.date(year=2019,month=8, day=1)
    month_days = Calendar().monthdatescalendar(2019, 8)
    context = request.args.get('matter','')
    get_date = request.args.get("day",'')
    designated_date = datetime.datetime.strptime(get_date, "%Y-%m-%d").day
    params = {
        'context':  context,
        'day': designated_date
    }
    week_name = ['月','火','水','木','金','土','日']
    
    return render_template(
        "index.html",month_day = month_days, week_name = week_name, month_current = month_current.month, params = params
    )

@app.route("/<int:post_id>")
def add_form(post_id):
    return render_template("create.html", des_id=post_id)

@app.route("/post", methods=["POST"])
def create():
    url = "http://localhost:3000/api/create"
    params = {
        "title": request.form['title'],
        "context": request.form['context'],
        "day": request.form['day']
    }
    json_request = requests.post(url, json=params)
    print(json_request.status_code)
    return redirect(url_for("index", matter=params['context'], day=params['day']))



if __name__ in "__main__":
    app.run(debug=True)