import time
import json


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myTest
coll = db.messageSensor

resp = {"type": "collection", "data":[]}
def makeResp (m, query):
  resp['data'] = []
  resp['query']=query
  for d in m:
    print d
    resp['data'].append(d)

def findClients ():
  print "findClients"
  m = coll.find().distinct("client")
  print m
  makeResp(m, "findClients")

def findTags (client):
    m = coll.find({'client':client}).distinct("name")
    makeResp(m, "findTags")

def findValsClientTag (client, tag):
    m= coll.find ({"client":client, "name": tag},{'ts':1,'val':1, '_id':0}).sort("ts",1).limit(10)
    makeResp(m, "findValsClientTag")

def findMinuteValsClientTag (client, tag):
    tmax = time.time()
    tmin = tmax - 60
    m = coll.find ({"client":client, "name": tag, "ts": {"$gte":tmin, "$lt":tmax}},{'ts':1,'val':1, '_id':0}).sort("ts",1)
    makeResp(m, "findMinuteValsClientTag")

def findHourValsClientTag (client, tag):
    tmax = time.time()
    tmin = tmax - 3600
    m= coll.find ({"client":client, "name": tag, "ts": {"$gte":tmin, "$lt":tmax}},{'ts':1,'val':1, '_id':0}).sort("ts",1)
    makeResp(m, "findHourValsClientTag")

def findLastValsClientTag (client, tag):
    m = coll.find({"client":client, "name":tag},{'ts':1,'val':1, '_id':0}).sort("ts",-1).limit(1)
    makeResp(m, "findLastValsClientTag")

# http://cookbook.mongodb.org/patterns/date_range/

def findByPeriod (client, min0, max0, sort):
  if ( max0 >= min0): 
    m= coll.find ({"client":client, "ts": {"$gt":min0, "$lt":max0}}).sort("ts",sort)
    makeResp (m, "findByPeriod")

def findMinute (client, ts, sort):
  tm = ts - 60
  findByPeriod (client, tm, ts, sort)
  
def findHour (client, ts, sort):
  tm = ts - 3600
  findByPeriod (client, tm, ts, sort)
 

def findlastMinute (client,sort):
   ts = time.time () - 60
   m = coll.find({"client":client, "ts": {"$gt":ts}}).sort("ts",sort)
   makeResp(m, "findlastMinute")

def findlastHour (client, sort):
   ts = time.time () - 3600 
   m = coll.find({"client":client, "ts": {"$gt":ts}}).sort("ts",sort)
   makeResp(m, "findlastHour")


def findLast (client):
   m = coll.find({"client":client}).sort("ts",-1).limit(1)
   makeResp(m, "findLast")
   
def findFirst (client):
   m = coll.find({"client":client}).sort("ts",1).limit(1)
   makeResp(m, "findFirst")


def calAverage (listVal):
   pass


def average (data):
  average = 0
  if len (resp['data']):
    for d in resp['data']:
      average += d['val']

    average = average/len(resp['data']) 
  print average

def averageLastHour (client):
  findlastHour (client,1)
  average (resp['data'])

def averageLastMinute (client):
  findlastMinute (client,1)
  average (resp['data'])


def mainT ():
  #findClients()
 
  #findLast ("pepe")

  #findFirst ("pepe")

  #findTags ("et001")

  #findByPeriod("pepe", 1403717170, 1403717212, 1)

  #findHour("pepe", 1403717170, 1)

  #averageLastMinute ("xaltu")
  #findValsClientTag ("pepe", "TE-01" )
  #findHourValsClientTag ("pepe", "TE-01")
  findLastValsClientTag ("pepe", "TE-01")
  print resp

if __name__ == "__main__":
  mainT()
  pass

