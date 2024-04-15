import json
from fastapi import FastAPI, Response
import redis
import os
import debugpy
from fastapi.templating import Jinja2Templates
from fasthx import Jinja
from .core.models.Reading import Reading

app = FastAPI()

r = redis.Redis(host="redis", port=6379)
debugpy.listen(("0.0.0.0", 5678))


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
	data = r.lrange("data", 0, 0)[0]
	item = json.loads(data)
	response = Reading(
		timestamp=item['timestamp'], 
		depth=item['depth'],
		temperature=item['temperature'], 
		barometer=item['barometer']
		)
	return response

@app.get("/status")
def get_status():
	last = r.get("last_logged")
	length = r.llen("data")
	return {"data_points": length, "last_logged": last}

@app.get("/current")
def get_current():
	data = r.lrange("data", 0, 0)[0]
	return json.loads(data)

@app.get("/data")
@jinja.page("data.html")
def get_data() -> list[Reading]:
	data = r.lrange("data", 0, 100)
	json_data = [json.loads(item) for item in data]
	response_data = [Reading(
		timestamp=item['timestamp'], 
		depth=item['depth'],
		temperature=item['temperature'], 
		barometer=item['barometer']
		) for item in json_data]
	return response_data