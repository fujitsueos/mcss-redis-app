import os

from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 7001))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port)


@app.route('/')
def index():
    return {'message': 'Hello, there!'}

@app.route('/api/redis')
def api_redis_get():
    value = redis_client.incr('counter', 1)
    return {'counter': value}
