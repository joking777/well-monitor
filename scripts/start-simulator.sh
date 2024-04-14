#!/bin/bash

echo starting socat

echo COMPOSE_PROFILES: $COMPOSE_PROFILES
echo LOG_LEVEL: $LOG_LEVEL
echo SERIAL_PORT: $SERIAL_PORT
echo BAUD_RATE: $BAUD_RATE
echo LOG_FREQUENCY: $LOG_FREQUENCY

echo Creating virtual serial port...
(socat pty,raw,echo=0,link=$SERIAL_PORT pty,raw,echo=0,link=/dev/ttyS21) &

until [ -L /dev/ttyS21 ]
do
    echo Checking if /dev/ttyS21 exists...
    sleep 3
done

echo Creating virtual serial port tunnel...
(socat /dev/ttyS21,raw,echo=0 TCP:well-monitor-monitor:4001) &

echo Starting simulator service...
/usr/local/bin/python /code/src/simulator.py