import redis
from flask import Flask, request, session, jsonify

db = None
app = Flask("proxies")


def init():
    global db
    db = redis.Redis(host="redis", port="6379", decode_responses=True)


def save():
    pass


if __name__ == "__main__":
    app.run(debut=True, host='0.0.0.0', port='8021')
