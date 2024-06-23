import os
import logging
from datetime import datetime
from core.models.Reading import Reading
from connections._redis_client import _redis_client
from connections.serial_port_client import serial_port_client

# Get the logger instance
from config._logger import _logger

log_level = os.environ.get('LOG_LEVEL', 'ERROR').upper()
serial_port = os.environ.get('SERIAL_PORT', '/dev/ttyUSB0')
# BAUD Rate in the context of a serial port is the number of bits that can be transferred per second
baud_rate = os.environ.get('BAUD_RATE', 19200)
data_size = os.environ.get('DATA_SIZE', 99)

# TODO - check if redis is connected

while serial_port_client.isOpen() != True:
    _logger.error('Waiting for port ' + serial_port)

while True:
    _logger.info("Monitor waiting for data...")
    #/r>>2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0/r/n
    timestamp = str(datetime.now())
    _redis_client.set("last_logged",timestamp)

    raw_data = serial_port_client.read_until()
    raw_data.strip()
    output = str(raw_data, encoding='utf-8', errors='ignore')

    reading = Reading(
        timestamp=output[3:22], 
        depth=float(output[29:36]),
        temperature=float(output[38:43]),
        barometer=float(output[45:50]),
        )
    
    _redis_client.lpush("data", reading.model_dump_json())
    _redis_client.ltrim("data", 0, data_size)

