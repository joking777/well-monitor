import json
from fastapi import FastAPI, Response
import os
from fastapi.templating import Jinja2Templates
from fasthx import Jinja
from .core.models.Reading import Reading
from .connections._redis_client import _redis_client

app = FastAPI()


basedir = os.path.abspath(os.path.dirname(__file__))

# Create the app instance.
app = FastAPI()

# Create a FastAPI Jinja2Templates instance. This will be used in FastHX Jinja instance.
templates = Jinja2Templates(directory=os.path.join(basedir, "templates"))

# FastHX Jinja instance is initialized with the Jinja2Templates instance.
jinja = Jinja(templates)


@app.get("/")
@jinja.page("index.html")
def index() -> Reading:
	data = _redis_client.lrange("data", 0, 0)[0]
	item = json.loads(data)
	response = Reading(
		timestamp=item['timestamp'], 
		depth=item['depth'],
		temperature=item['temperature'], 
		barometer=item['barometer']
		)
	return response

@app.get("/api/status")
def get_status():
	last = _redis_client.get("last_logged")
	length = _redis_client.llen("data")
	return {"data_points": length, "last_logged": last}

@app.get("/api/current")
def get_current():
	data = _redis_client.lrange("data", 0, 0)[0]
	return json.loads(data)

@app.get("/data")
@jinja.page("data.html")
def get_data() -> list[Reading]:
	data = _redis_client.lrange("data", 0, 100)
	json_data = [json.loads(item) for item in data]
	response_data = [Reading(
		timestamp=item['timestamp'], 
		depth=item['depth'],
		temperature=item['temperature'], 
		barometer=item['barometer']
		) for item in json_data]
	return response_data