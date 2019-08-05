from flask import Flask, jsonify, render_template, redirect, request, url_for
import calendar
from calendar import Calendar
import os
import datetime

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
    now = datetime.date.today()
    month_current = datetime.date(year=2019,month=8, day=1)
    month_days = Calendar().monthdatescalendar(2019, 8)
    month_before = datetime.date(year=2019, month=7, day=1)
    month_next = datetime.date(year=2019, month=9, day=1)
    week_name = ['月','火','水','木','金','土','日']

    return render_template(
        "index.html",month_day = month_days, week_name = week_name, month_current = month_current.month
    )






if __name__ in "__main__":
    app.run(debug=True)