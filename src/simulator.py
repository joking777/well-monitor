import os
import logging
import time
from datetime import datetime
from connections.serial_port_client import serial_port_client
from config._logger import _logger

MIN_DEPTH=50
MAX_DEPTH=250
DEPTH_INCREMENTS=.5

log_level = os.environ.get('LOG_LEVEL', 'ERROR').upper()
serial_port = os.environ.get('SERIAL_PORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUD_RATE', 19200)
log_frequency = os.environ.get('LOG_FREQUENCY', 10)

_logger.info("Starting simulator...")

if serial_port_client.isOpen() != True:
    serial_port_client.open()

_logger.info("Simulator opened serial port " + serial_port + "...")

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    timestamp = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    output = ">>" + timestamp + " #000 D  34.38 T 75.0 B16.27 G729 R 0"
    _logger.debug(output)
    output = "\r" + output + "\r\n"
    serial_port_client.write(output.encode())
    _logger.debug("Sleeping for " + str(log_frequency) + " seconds")
    time.sleep(int(log_frequency))
