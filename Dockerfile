FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
#COPY ./scripts/monitor.service /etc/systemd/system/monitor.service

COPY ./scripts/start-monitor.sh /start-monitor.sh
RUN chmod +x /start-monitor.sh

COPY ./scripts/start-simulator.sh /start-simulator.sh
RUN chmod +x /start-simulator.sh

RUN apt-get update && apt-get install -y systemctl socat iputils-ping

