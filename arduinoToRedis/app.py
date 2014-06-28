# 
# To see how to interface arduino with python scripts
# http://playground.arduino.cc/Interfacing/Python
#
import time
import redis
import json
import serial

conn = redis.Redis('localhost')
redisList = "mylist"

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    #parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1
)

#
#  send message to Arduino
#
def sendMessage (messS):
  ser.flushInput()
  ser.write(str(messS))



if __name__ == '__main__':
  client = "arduino"
  name = "TE-03"
  sendMessage('a')
  while 1:
    time.sleep(1)
    sendMessage('a')
    val = ser.readline().strip()
    a={'client':client, 'val': val, 'name':name, 'ts':time.time()}
    conn.lpush (redisList,json.dumps(a))
    print a



