import os
import logging
import time
import serial
from datetime import datetime

MIN_DEPTH=50
MAX_DEPTH=250
DEPTH_INCREMENTS=.5

log_level = os.environ.get('LOGLEVEL', 'ERROR').upper()
serial_port = os.environ.get('SERIALPORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUDRATE', 19200)

serial_port = '/dev/ttyS20'

logging.basicConfig(
    level=log_level,
    format='%(levelname)s\t%(message)s'
)

print("Starting simulator...")

# import serial.tools.list_ports
# print(list(serial.tools.list_ports.comports()))

# ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#         print("{}: {} [{}]".format(port, desc, hwid))

w = serial.Serial(serial_port, baud_rate, write_timeout=0)

if w.isOpen() != True:
    w.open()

print("Opened serial port...")

while True:
    #2023/04/10 19:21:11 #000 D  34.38 T 75.0 B16.27 G729 R 0
    timestamp = str(datetime.now())
    output = timestamp + " #000 D  34.38 T 75.0 B16.27 G729 R 0"
    print(output)
    output = output + '\r\n'
    w.write(output.encode())
    # w.write(bytes(output, 'utf-8'))
    # w.write(b'S')
    logging.info(output)
    print("Sleeping")
    time.sleep(1)
