import os
import logging
import time
import serial
from datetime import datetime
import redis

log_level = os.environ.get('LOGLEVEL', 'INFO').upper()
redis_host = os.environ.get('REDISHOST', 'redis')
redis_port = os.environ.get('REDISPORT', 6379)
serial_port = os.environ.get('SERIALPORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUDRATE', 19200)

logging.basicConfig(
    level=log_level
    format='%(levelname)s\t%(message)s'
)

r = redis.Redis(host=redis_host, port=redis_port)
l = serial.Serial(serial_port, baud_rate, timeout=None)

# TODO - check if redis is connected

if serial_port != 'simulate':
    if l.isOpen() != True:
        logging.error('Error openening serial port ' + serial_port)

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    timestamp = str(datetime.now())
    r.set("last_logged",timestamp)

    output = timestamp + " #000 D  34.38 T 75.0 B16.27 G729 R 0"
    if serial_port != 'simulate':
        raw_data = l.read_until()
        raw_data.trim()
        output = str(raw_data)
    logging.info(output)
    r.lpush("data", output)

    if serial_port == 'simulate':
        time.sleep(1)
