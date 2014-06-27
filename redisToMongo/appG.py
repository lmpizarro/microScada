#  http://sdiehl.github.io/gevent-tutorial/
import gevent
import signal



import logging

import threading
import redis
import time
import json
import pymongo

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

client = pymongo.MongoClient('localhost', 27017)
db = client.myTest
coll = db.messageSensor

print coll

conn = redis.StrictRedis('localhost')


def worker (delay):
  logging.debug('Starting')
  while 1:
   time.sleep(delay)
   ts = time.time()
   logging.debug("worker %d"% (ts))
   while conn.llen('mylist') !=0:
     m = conn.lpop('mylist')
     id = coll.insert (json.loads(m))
     print m


def main ():
  delay = 10
  gevent.signal(signal.SIGQUIT, gevent.kill)
  thread = gevent.spawn(worker (delay))
  thread.join()


if __name__ == "__main__": main()

