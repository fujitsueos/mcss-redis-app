import os

from flask import Flask, render_template
import redis

template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir)
app_name = os.environ.get('APP_NAME', 'dev')

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 7001))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

def counter():
    return redis_client.incr('counter', 1)


@app.route('/')
def index():
    visit_count = counter()
    return render_template('index.html', app_name=app_name, visitors=visit_count)

@app.route('/api/redis')
def api_redis_get():
    visit_count = counter()
    return {'counter': visit_count}
