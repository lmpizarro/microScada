import threading
import random
import time
import redis
import json

conn = redis.Redis('localhost')


def worker (delay, mu, sigma, client,name):
  a={'client':client, 'val': '', 'name':name}
  n= 0
  while 1:
    n +=1
    a['val'] = random.gauss(mu, sigma)
    ts = time.time()
    a['ts'] = ts
    conn.lpush ('mylist',json.dumps(a))
    time.sleep(delay)


def main ():
  delay = 10
  mu = 2
  sigma = .1
  client="et001"
  tag = "TE-02"
  t = threading.Thread(name="worker", target=worker, args=(delay,mu,sigma,client,tag))
  t.setDaemon(True)
  s = threading.Thread(name="worker", target=worker, args=(5,1,.01,client,"TE-01"))
  s.setDaemon(True)
  s.start()
  t.start()


if __name__ == "__main__": 
  main()
  d = threading.Thread(name="worker", target=worker, args=(3,3,.2,"pepe","TE-01"))
  #d.setDaemon(True)
  d.start()
  #d.join()
  #t.join()


