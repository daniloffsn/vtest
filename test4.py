#!/usr/bin/python
# -*- coding: UTF-8 -*-

from websocket import create_connection
import sys

if len (sys.argv) > 1:
 first = int(sys.argv[1])
else:
  first = int(raw_input("Enter the first no:"))

if len (sys.argv) > 2:
 second = int(sys.argv[2])
else:
 second = int(raw_input("Enter Second no:"))

print first
print second




#first = int(raw_input("Enter the first no:"))
#second = int(raw_input("Enter Second no:"))

def echows(N):
  ws = create_connection("ws://localhost/echo")
  for i in range(1, N+1):
     hello = "Hello " + str(i) + " times"
     print "Sending", hello
     ws.send(hello)
     result =  ws.recv()
     print "Received '%s'" % result
  ws.close()

for j in range(1, first+1):
   print "Connection", j
   echows(second)
