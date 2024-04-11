import os
import logging
import time
from datetime import datetime
import redis
import serial.tools.list_ports;

logging.basicConfig(
    level=os.environ.get('LOGLEVEL', 'INFO').upper(),
    format='%(levelname)s\t%(message)s'
)

r = redis.Redis(host="redis", port=6379)

#ports = serial.tools.list_ports.comports()

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    # TODO: read from serial port
    timestamp = str(datetime.now())
    r.set("last_logged",timestamp)
    output = timestamp + " #000 D  34.38 T 75.0 B16.27 G729 R 0"
    logging.info(output)
    r.lpush("data", output)
    time.sleep(1)
