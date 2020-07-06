import os
import json
from pymemcache.client.base import Client

CACHE_MEMCACHED_SERVER = os.environ.get('MEMCACHED_SERVER', '94.103.94.54')
CACHE_MEMCACHED_PORT = os.environ.get('MEMCACHED_PORT', 11211)


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2


def json_deserializer(key, value, flags):
    if flags == 1:
        return value.decode("utf-8")
    if flags == 2:
        return json.loads(value.decode("utf-8"))
    raise Exception("Unknown serialization format")


client = Client(
    (CACHE_MEMCACHED_SERVER, CACHE_MEMCACHED_PORT),
    serializer=json_serializer,
    deserializer=json_deserializer
)

if __name__ == "__main__":
    try:
        result = client.get('key')
        print(result)
    except:
        client.set('key', {'a': 'b', 'c': 'd'})
        result = client.get('key')
        print(result)
