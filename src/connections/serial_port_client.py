import os
import time
import serial
# Serial port settings
port_name = os.environ.get('SERIAL_PORT', '/dev/ttyUSB0')
baud_rate = os.environ.get('BAUD_RATE', 19200)
timeout = 1  # Timeout in seconds
max_retry_attempts = 3  # Maximum number of retry attempts

def connect_serial():
    attempt = 0
    while attempt < max_retry_attempts:
        try:
            # Create a serial port instance
            serial_port = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout, write_timeout=0)
            print("Serial port connected successfully.")
            return serial_port

        except serial.SerialException as e:
            attempt += 1
            print(f"Failed to connect to serial port (Attempt {attempt}/{max_retry_attempts}): {e}")
            time.sleep(1)  # Wait for a short duration before retrying
    return None  # Return None if connection fails after maximum attempts

# Attempt to connect to serial port
serial_port_client = connect_serial()
