from fastapi import FastAPI, Response
import redis
import os
import debugpy
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from fasthx import Jinja

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
def index() -> None:
    """This route serves the index.html template."""
    ...

@app.get("/status")
def read_root():
	last = r.get("last_logged")
	length = r.llen("data")
	return {"data_points": length, "last_logged": last}

@app.get("/data")
def read_root():
	data = r.lrange("data", 0, 100)
	return {"data": data} 