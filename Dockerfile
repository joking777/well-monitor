FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY ./scripts/monitor.service /etc/systemd/system/monitor.service
COPY ./scripts/start.sh /start.sh

RUN chmod +x /start.sh
RUN apt-get update && apt-get install -y systemctl
