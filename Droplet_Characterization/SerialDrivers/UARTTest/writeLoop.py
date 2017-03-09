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

print "Serial is open: " + str(ser.isOpen())

for writeIterator in range(10):
	print "Now Writing", writeIterator
	ser.write("Test: ")
	ser.write(str(writeIterator))
	ser.write('\r\n')

#ser.write("Begin running program\r\n")

print "Finished write, now closing"

ser.close()
