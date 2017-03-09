import serial
import time
import subprocess

class VulcanSerial:
	def __init__(self, portDes='/dev/ttyS0', baud=115200, timeOut=1, lineEndings = '\r\n'):
		self.serialPort = serial.Serial(
			port = portDes,
			baudrate = baud,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout = timeOut
		)

		self.lineEndings = lineEndings

	def tryRead(self):
		try:
			x = self.serialPort.read()
			time.sleep(1)
			dataLeft = ser.inWaiting()
			x += ser.read(dataLeft)
			x = ''.join(c for c in x if c.isalnum())
			return x

		except Exception as e:
			print e
			return False

	def tryWrite(self, itemToWrite):
		try:
			ser.write(str(itemToWrite))
			ser.write(self.lineEndings)
			return True

		except Exception as e:
			print e
			return False

	def closePorts(self):
		self.serialPort.close()	
