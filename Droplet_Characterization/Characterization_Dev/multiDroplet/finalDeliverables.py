import subprocess
import os
import serial
import time
import os
import signal
#with open('testLogs.log', 'w') as f:
# Passing params through execve

ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)

started = False
pid = ''
proc = ''

while True:

	line = ''
	x = ser.read()
	time.sleep(1)
	dataLeft = ser.inWaiting()
	x += ser.read(dataLeft)	
	print(x)	

	if x == 'Beginrunningprogram':
		proc = subprocess.Popen(['python', '-u', 'FinalDeliverables.py', '-v', 'BlueAndRed.m4v'], stdout=subprocess.PIPE)
	
		pid = proc.pid
		line = proc.stdout.readline()
		started = True
	elif (x == 'kill' and pid != ''):
		os.kill(pid, signal.SIGINT)
		
		if not proc.poll():
			print "Process correctly halted"
			ser.write("Process correctly halted")
			ser.write('\r\n')

	if started == True:
		line = proc.stdout.readline()

	if line != '':
		print line
		ser.write(line)
		ser.write('\r\n')

#def execute(cmd):
#	p = subprocess.Popen(cmd, stdout = subprocess.PIPE, universal_newlines=True)

#	for stdout_line in iter(p.stdout.readline, ""):
#		yield stdout_line

#	p.stdout.close()
#	return_code = p.wait()

#	if return_code:
#		raise subprocess.CalledProcessError(return_code, 'stdOutLoop.py')

#while True:
#	print "lolhi"
#	for path in execute(['python','-u',  'stdOutLoop.py']):
#		print path,
