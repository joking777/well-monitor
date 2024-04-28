import logging
from logging.handlers import RotatingFileHandler
import datetime

# Create logger
_logger = logging.getLogger("app")
_logger.setLevel(logging.DEBUG)

# Create console handler and set level to INFO
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.INFO)

# Create file handler and set level to DEBUG, with rotation once a week
fileHandle = RotatingFileHandler('app.log', mode='a', maxBytes=100000, backupCount=3)
fileHandle.setLevel(logging.DEBUG)

# Setup the formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandle.setFormatter(formatter)
fileHandle.setFormatter(formatter)

# Add handlers to logger
_logger.addHandler(consoleHandle)
_logger.addHandler(fileHandle)