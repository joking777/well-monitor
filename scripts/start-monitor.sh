#!/bin/bash

# echo starting socat null modem
# (socat pty,raw,echo=0,link=/dev/ttyS20 pty,raw,echo=0,link=/dev/ttyS21) &

# echo starting socat tcp listener
# (socat open:/dev/ttyS21,nonblock,echo=0,raw TCP-LISTEN:4001,reuseaddr,fork) &

# (socat TCP4-LISTEN:4001,reuseaddr,fork SYSTEM:"/dev/ttyS20,raw.echo=0") &
# socat TCP-LISTEN:4001,reuseaddr,fork SYSTEM:"/dev/ttyS20"
# socat TCP-LISTEN:4001,reuseaddr,fork PTY,link=/dev/ttyS20

echo starting monitor service
/usr/local/bin/python /code/src/monitor.py