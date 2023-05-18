import redis

# Create a Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)