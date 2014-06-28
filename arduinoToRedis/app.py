import time
import redis
import json


conn = redis.Redis('localhost')
redisList = "mylist"

client = "arduino"
val    =  12345
name = "TE-03"

a={'client':client, 'val': val, 'name':name, 'ts':time.time()}


conn.lpush (redisList,json.dumps(a))
