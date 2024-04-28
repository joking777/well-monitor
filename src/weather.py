import os
import logging
import redis
import time
from datetime import datetime, timedelta

log_level = os.environ.get('LOG_LEVEL', 'ERROR').upper()
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = os.environ.get('REDIS_PORT', 6379)

logging.basicConfig(
    level=log_level,
    format='%(levelname)s\t%(message)s'
)

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

HOUR_IN_SECONDS = 60 * 60
MINUTE_IN_SECONDS = 60;
DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

r.set('weather_forecast_next_check', str(datetime.now() + timedelta(minutes=1)))

while True:
    logging.info("Checking weather data...")
    timestamp = datetime.now()
    next_check_str = r.get('weather_forecast_next_check')

    logging.info(next_check_str)

    if next_check_str != None:
        next_check = datetime.strptime(next_check_str, DEFAULT_TIME_FORMAT)

        logging.info("Next check: " + str(next_check))
        logging.info("Current time: " + str(timestamp))

        if next_check < timestamp:
            logging.info("Calling weather API...")
            r.set('weather_forecast_last_check', str(timestamp))
            r.set('weather_forecast_next_check', str(timestamp + timedelta(minutes=1)))
    
    time.sleep(MINUTE_IN_SECONDS)