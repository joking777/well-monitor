#!/bin/bash

echo COMPOSE_PROFILES: $COMPOSE_PROFILES
echo LOG_LEVEL: $LOG_LEVEL
echo SERIAL_PORT: $SERIAL_PORT
echo BAUD_RATE: $BAUD_RATE
echo LOG_INTERVAL: $LOG_INTERVAL

if [[ "$COMPOSE_PROFILES" =~ "simulate" ]]; then

    echo Creating virtual serial port...
    (socat pty,raw,echo=0,link=$SERIAL_PORT pty,raw,echo=0,link=/dev/ttyS21) &

    until [ -L /dev/ttyS21 ]
    do
        echo Checking if /dev/ttyS21 exists...
        sleep 3
    done
    echo Creating virtual serial port tunnel...
    (socat open:/dev/ttyS21,nonblock,echo=0,raw TCP-LISTEN:4001,reuseaddr,fork) &
fi

echo starting monitor service
/usr/local/bin/python /code/src/monitor.py