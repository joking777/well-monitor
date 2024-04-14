#!/bin/bash

echo starting socat
# socat pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21
# socat pty,link=/dev/ttyS20,raw tcp:monitor:4001
# socat SYSTEM:"/dev/ttyS20,raw,echo=0" TCP:monitor:4001
(socat /dev/ttyS20,raw,echo=0 TCP:well-monitor-monitor:4001) &
# socat /dev/ttyS20,raw,echo=0 TCP:172.20.0.4:4001


# socat TCP4-LISTEN:4001,reuseaddr,fork SYSTEM:"/dev/ttyS20,raw.echo=0"

echo starting simulator service
/usr/local/bin/python /code/src/simulator.py