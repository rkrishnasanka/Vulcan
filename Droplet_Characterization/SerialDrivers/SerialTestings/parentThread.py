import subprocess
import os
#with open('testLogs.log', 'w') as f:
# Passing params through execve

proc = subprocess.Popen(['python', '-u', 'stdOutLoop.py'], stdout=subprocess.PIPE)

while True:
	line = proc.stdout.readline()

	if line != '':
		print line

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
