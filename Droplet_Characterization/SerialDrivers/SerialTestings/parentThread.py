import subprocess
import sys

#with open('testLogs.log', 'w') as f:
# Passing params through execve
process = subprocess.Popen(['python', 'stdOutLoop.py'], stdout = subprocess.PIPE)
#process = subprocess.Popen('python stdOutLoop.py', shell=True).wait()
for line in iter(process.stdout.readline, ''):
	print line
