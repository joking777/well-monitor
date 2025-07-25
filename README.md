# Well Monitor

The well monitor project is intended to create a docker container to run on a Raspberry Pi to read and access data from a well monitor with a serial interface.

## Installation

Download this project and run.

Add the following `.env` to run in simulation mode
```
LOG_LEVEL=INFO
SERIAL_PORT=/dev/ttyS20
COMPOSE_PROFILES=simulate
```

```bash
docker-compose up --build
```

### Raspberry Pi

Install docker

https://devops.stackexchange.com/questions/5192/how-to-install-docker-in-raspbian-virtual-machine

```
apt install docker.io
```

Install docker-compose

https://medium.com/@vinothsubramanian/how-to-install-docker-compose-in-raspberry-pi-4a11e6314bbb

```
sudo curl -L https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-`uname -s`-`uname -m` > docker-compose
sudo mv docker-compose /usr/bin/
sudo chown root: /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compos
```

Docker permissions

https://phoenixnap.com/kb/docker-permission-denied

```
sudo groupadd -f docker
sudo usermod -aG docker $USER
newgrp docker
```

```bash
docker-compose -f docker-compose.yml -f docker-compose-live.yml up --build
```

## Monitor Process

The monitor process will run in a separate container

## API

### Status

https://localhost/api/status

### Current Data

https://localhost/api/current

## Utitlities

On MacOS you can find the serialusb connection by

```
ls /dev/tty.*
```

and connect using `cu`

```
sudo cu -s 19200 -l /dev/tty.usbserial-A6005kdh
```

On Raspberry Pi to download the logged data

```
screen /dev/ttyUSB0 19200
```

## Inspiration

- https://www.youtube.com/watch?v=6OxqiEeCvMI
- https://www.youtube.com/watch?v=AHr94RtMj1A
- https://gist.github.com/stonehippo/e33750f185806924f1254349ea1a4e68

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
