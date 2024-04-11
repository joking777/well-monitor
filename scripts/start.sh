#!/bin/bash

# install the monitor service
systemctl daemon-reload
systemctl enable monitor.service
systemctl start monitor.service