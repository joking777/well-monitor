import redis
import os

host = os.environ.get('REDIS_HOST', 'redis')
port = os.environ.get('REDIS_PORT', 6379)

redis_pool = redis.ConnectionPool(host=host, port=port, db=0, max_connections=10)

# Create the Redis client
_redis_client = redis.Redis(connection_pool=redis_pool)