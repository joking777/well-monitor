#!/bin/bash

echo COMPOSE_PROFILES: $COMPOSE_PROFILES
echo LOG_LEVEL: $LOG_LEVEL
echo WEATHER_API_KEY: $WEATHER_API_KEY
echo LAT_LON: $LAT $LON

echo starting weather service
/usr/local/bin/python /code/src/weather.py