#!/usr/bin/env python
import serial
import time
ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

#print "Serial is open: " + str(ser.isOpen())

#print "Now Writing"
#ser.write("This is a test")

#print "Did write, now read"
while True:
	x = ser.read()
	time.sleep(1)
	dataLeft = ser.inWaiting()
	x += ser.read(dataLeft)
	print "got '" + x + "'"

ser.close()
