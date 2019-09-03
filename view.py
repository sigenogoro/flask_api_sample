from flask import Flask, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime
import requests
import json

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
    url_info = "http://127.0.0.1:3000/api/index"
    month_current = datetime.date(year=2019,month=8, day=1)
    month_days = Calendar().monthdatescalendar(2019, 8)
    context_json = requests.get(url_info).text
    week_name = ['月','火','水','木','金','土','日']
    if json.loads(context_json):
        title = json.loads(context_json)[0]["title"]
        get_date = requests.get(url_info).text
        designated_date = json.loads(get_date)[0]["day"]
        params = {
            'context':  title,
            'day': datetime.datetime.strptime(designated_date,"%Y-%m-%d").day
        }
        return render_template(
            "index.html",month_day = month_days, week_name = week_name, month_current = month_current.month, params = params
        )
    return render_template(
        "index.html",month_day = month_days, week_name = week_name, month_current = month_current.month
    )

@app.route("/<int:post_id>")
def add_form(post_id):
    url_info = "http://127.0.0.1:3000/api/index"
    json_data = requests.get(url_info).text
    if json.loads(json_data):
        get_id = json.loads(json_data)[0]['day']
        day = datetime.datetime.strptime(get_id,"%Y-%m-%d").day
        if day == post_id:
            params = {
                "title": json.loads(json_data)[0]['title'],
                "context": json.loads(json_data)[0]['context']
            }
            return render_template("edit.html", des_id=post_id, params=params)
        else:
            return render_template("create.html", des_id=post_id)
    else:
        return render_template("create.html", des_id=post_id)

@app.route("/post", methods=["POST"])
def create():
    if request.form.get('_method') == "POST":
        url = "http://127.0.0.1:3000/api/create"
        params = {
            "title": request.form['title'],
            "context": request.form['context'],
            "day": request.form['day']
        }
        requests.post(url, params=params)
        return redirect(url_for("index"))
    elif request.form.get('_method') == "put":
        edit_url = "http://127.0.0.1:3000/api/edit"
        params = {
            "title": request.form['title'],
            "context": request.form['context'],
            "day": request.form['day']
        }
        requests.put(edit_url, params=params)
        return redirect(url_for("index"))

#PUTやDELETEはできないらしいため、methods=["POST"]にしています（HTMLのFormからは、読み取れないらしい）
@app.route("/delete", methods=["POST"])
def all_delete():
    if request.form.get("_method") == "DELETE":
        delete_url = "http://127.0.0.1:3000/api/delete"
        requests.delete(delete_url)
        return redirect(url_for("index"))





if __name__ in "__main__":
    app.run(debug=True)