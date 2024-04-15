import os
import logging
import time
import serial
from datetime import datetime

MIN_DEPTH=50
MAX_DEPTH=250
DEPTH_INCREMENTS=.5

log_level = os.environ.get('LOG_LEVEL', 'ERROR').upper()
serial_port = os.environ.get('SERIAL_PORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUD_RATE', 19200)
log_frequency = os.environ.get('LOG_FREQUENCY', 10)

logging.basicConfig(
    level=log_level,
    format='%(levelname)s\t%(message)s'
)

logging.info("Starting simulator...")

w = serial.Serial(serial_port, baud_rate, write_timeout=0)

if w.isOpen() != True:
    w.open()

logging.info("Simulator opened serial port " + serial_port + "...")

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    output = ">>" + timestamp + " #000 D  34.38 T 75.0 B16.27 G729 R 0"
    logging.info(output)
    output = "\r" + output + "\r\n"
    w.write(output.encode())
    logging.info("Sleeping for " + str(log_frequency) + " seconds")
    time.sleep(int(log_frequency))
