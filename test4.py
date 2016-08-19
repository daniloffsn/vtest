#!/usr/bin/python
# -*- coding: UTF-8 -*-

from websocket import create_connection
import sys

if len (sys.argv) > 2:
 first = int(sys.argv[1])
 second = int(sys.argv[2])
 print first
 print second
else:
 print ("No paramerers!")




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

for j in range(first):
   echows(second)
