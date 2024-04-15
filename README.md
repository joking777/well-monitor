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

## Monitor Process

The monitor process will run in a separate container

## API

### Status

https://localhost/status

### Data

https://localhost/data

## Utitlities

On MacOS you can find the serialusb connection by

```
ls /dev/tty.*
```

and connect using `cu`

```
sudo cu -s 19200 -l /dev/tty.usbserial-A6005kdh
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
