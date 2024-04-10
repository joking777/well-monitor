from fastapi import FastAPI
import redis
import debugpy

app = FastAPI()

r = redis.Redis(host="redis", port=6379)
debugpy.listen(("0.0.0.0", 5678))
#debugpy.wait_for_client()

@app.get("/")
def read_root():
	return {"Hello": "World!"}

@app.get("/hits")
def read_root():
	r.incr("hits")
	return {"number of hits", r.get("hits")}