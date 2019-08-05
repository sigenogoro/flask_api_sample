from flask import Flask, jsonify, render_template, redirect, request


app = Flask(__name__)

users = [
    { "id": 1, "add_plan": "彼女とデート" },
    { "id": 2, "add_plan": "試験対策" },
    { "id": 3, "add_plan": "練習" },
    {"id":4, "add_plan": "スペイン旅行"}
]


@app.route("/api/index")
def schedule_index():
    index = users
    pass


@app.route("/api/add_plan", methods=["POST"])
def create():
    return jsonify(request.form)


@app.route("/api/detail", methods=["GET"])
def detail():
    return jsonify(request.form)

if __name__ in "__main__":
    app.run(debug=True, threaded=True, port=3000, host="localhost")