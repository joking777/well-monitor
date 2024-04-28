#!/bin/bash

source ../.env

if [ $WEATHER_API_KEY == "" ]; then
  echo $WEATHER_API_KEY not defined
  exit
fi

echo $WEATHER_API_KEY

# documentation
# https://openweathermap.org/api

# current weather
# curl -s https://api.openweathermap.org/data/3.0/onecall?lat=$LAT&lon=$LON&appid=$WEATHER_API_KEY

# time machine
# curl https://api.openweathermap.org/data/3.0/onecall/timemachine?lat=39.099724&lon=-94.578331&dt=1643803200&appid=$WEATHER_API_KEY
