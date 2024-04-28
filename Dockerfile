FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

COPY ./scripts/start-monitor.sh /start-monitor.sh
RUN chmod +x /start-monitor.sh

COPY ./scripts/start-simulator.sh /start-simulator.sh
RUN chmod +x /start-simulator.sh

COPY ./scripts/start-weather.sh /start-weather.sh
RUN chmod +s /start-weather.sh

RUN apt-get update && apt-get install -y cu socat iputils-ping

