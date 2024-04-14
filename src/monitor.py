import os
import logging
import time
import serial
from datetime import datetime
import redis
import json

log_level = os.environ.get('LOGLEVEL', 'ERROR').upper()
redis_host = os.environ.get('REDISHOST', 'redis')
redis_port = os.environ.get('REDISPORT', 6379)
serial_port = os.environ.get('SERIALPORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUDRATE', 19200)

logging.basicConfig(
    level=log_level,
    format='%(levelname)s\t%(message)s'
)

r = redis.Redis(host=redis_host, port=redis_port)
l = serial.Serial(serial_port, baud_rate, timeout=None)

# TODO - check if redis is connected

while l.isOpen() != True:
    logging.error('Waiting for port ' + serial_port)

print("Get data now...")

r.ltrim("data")

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    timestamp = str(datetime.now())
    r.set("last_logged",timestamp)

    raw_data = l.read_until()
    raw_data.strip()
    output = str(raw_data, encoding='utf-8')

    obj = {
        "timestamp": output[3:22],
        "depth": float(output[29:36]),
        "temperature": float(output[38:43]),
        "barometer": float(output[45:50])
    }

    json_str = json.dumps(obj)

    logging.info(json_str)
    r.lpush("data", json_str)
