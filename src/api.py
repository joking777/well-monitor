from fastapi import FastAPI
import redis
import debugpy

app = FastAPI()

r = redis.Redis(host="redis", port=6379)
debugpy.listen(("0.0.0.0", 5678))

@app.get("/")
def read_root():
	return {"Hello": "World!"}

@app.get("/status")
def read_root():
	last = r.get("last_logged")
	length = r.llen("data")
	return {"data_points": length, "last_logged": last}

@app.get("/data")
def read_root():
	data = r.lrange("data", 0, 100)
	return {"data": data} 