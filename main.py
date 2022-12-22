from flask import Flask, jsonify, abort
import os
days = [
    {"id": 1, "name": "Monday"},
    {"id": 2, "name": "Tuesday"},
    {"id": 3, "name": "Wednesday"},
    {"id": 4, "name": "Thursday"},
    {"id": 5, "name": "Friday"},
    {"id": 6, "name": "Saturday"},
    {"id": 7, "name": "Sunday"},
]

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_days():
    return jsonify(days)


@app.route("/", methods=["POST"])
def post_days():
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    app.run(host=os.environ.get('APP_HOSTNAME', '0.0.0.0'),
            port=os.environ.get('APP_PORT', '8080'))