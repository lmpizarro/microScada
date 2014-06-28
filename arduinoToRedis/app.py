# 
# To see how to interface arduino with python scripts
# http://playground.arduino.cc/Interfacing/Python
#
import time
import redis
import json


conn = redis.Redis('localhost')
redisList = "mylist"

client = "arduino"
val    =  12345 # this val comes from arduino
name = "TE-03"

a={'client':client, 'val': val, 'name':name, 'ts':time.time()}


conn.lpush (redisList,json.dumps(a))
