import threading
import random
import time
import redis
import json

conn = redis.Redis('localhost')
redisList = "mylist"

class PeriodicSensor ():
  # http://stackoverflow.com/questions/8600161/executing-periodic-actions-in-python

  def __init__ (self, client, id, delay, mu, sigma):
    self.next_call = time.time()
    self.delay = delay
    self.id = id
    self.client = client
    self.mu = mu
    self.sigma = sigma


  def worker(self):
    a={'client':self.client, 'val': random.gauss(self.mu, self.sigma), 'name':self.id, 'ts':time.time()}
    print a 
    conn.lpush (redisList,json.dumps(a))
    self.next_call = self.next_call + self.delay
    threading.Timer( self.next_call - time.time(), self.worker ).start()



if __name__ == "__main__": 
  foo  = PeriodicSensor ("pepe", "TE-01" , 2, 3.0, 0.1)
  boo  = PeriodicSensor ("altu", "TE-01" ,3, 1.0, 0.1)
  xoo  = PeriodicSensor ("altu", "TE-02" ,5, 1.0, 0.1)
  coo  = PeriodicSensor ("pepe", "TE-02" ,10, 1.0, 0.1)

  foo.worker()
  boo.worker()
  xoo.worker()
  coo.worker()
