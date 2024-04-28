import os
import time
import requests
import json
from datetime import datetime, timedelta
from connections._redis_client import _redis_client

# Get the logger instance
from config._logger import _logger

api_url = os.environ.get('WEATHER_API_URL')
api_key = os.environ.get('WEATHER_API_KEY')
lat = os.environ.get('LAT')
lon = os.environ.get('LON')

HOUR_IN_SECONDS = 60 * 60
MINUTE_IN_SECONDS = 60
DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
URL=f'{api_url}?lat={lat}&lon={lon}&appid={api_key}'

if api_key == None:
    _logger.error('Weather api not set in .env file')
else:
    _logger.info('Weather lookup url: ' + URL)

while api_key != None:
    _logger.info('Checking weather data...')
    timestamp = datetime.now()
    next_check_str = _redis_client.get('weather_forecast_next_check')

    _logger.info('Next weather check: ' + next_check_str)

    if next_check_str != None:
        next_check = datetime.strptime(next_check_str, DEFAULT_TIME_FORMAT)

        if next_check < timestamp:
            _logger.info('Calling weather API...')
            response = requests.get(URL)
            if(response.status_code == 200):
                _redis_client.set('weather_forcast', json.dumps(response.json()))
            else:
                _logger.error('Response code: ' + str(response.status_code))

            _redis_client.set('weather_forecast_last_check', str(timestamp))
            _redis_client.set('weather_forecast_next_check', str(timestamp + timedelta(minutes=1)))
    
    time.sleep(MINUTE_IN_SECONDS)