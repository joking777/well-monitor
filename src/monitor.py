import os
import logging
import time
from datetime import datetime
import redis
import serial.tools.list_ports;

# Local Imports
from parse_script import parse_log

logging.basicConfig(
    level=os.environ.get('LOGLEVEL', 'INFO').upper(),
    format='%(levelname)s\t%(message)s'
)

r = redis.Redis(host="redis", port=6379)

# ports = serial.tools.list_ports.comports()

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    # TODO: read from serial port
    parsed_timestamp, parsed_depth, parsed_log = parse_log("2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0")

    #timestamp = str(datetime.now())
    r.set("last_logged", str(parsed_timestamp))
    logging.info(parsed_log)
    r.lpush("data", parsed_log)
    time.sleep(1)
