import time
import redis
from flask import Flask
from datetime import datetime
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def obtener_la_ultima_visita():
    try:
        ultima_visita = cache.getset('ultima_visita', str(datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
        if ultima_visita is None:
            return cache.getset('ultima_visita',str(datetime.now().strftime("%Y-%m-%d, %H:%M:%S")))
        return ultima_visita
    except redis.exceptions.ConnectionError as e:
        raise e
@app.route('/')

def index():
    ultima_visita = str(obtener_la_ultima_visita().decode('utf-8'))
    return 'Practicas Modernas con Docker! Visitado el {}.\n'.format(ultima_visita)
