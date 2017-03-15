import subprocess

#with open('testLogs.log', 'w') as f:
# Passing params through execve

def execute(cmd):
	p = subprocess.Popen(cmd, stdout = subprocess.PIPE, universal_newlines=True)

	for stdout_line in iter(p.stdout.readline, ""):
		yield stdout_line

	p.stdout.close()
	return_code = p.wait()

	if return_code:
		raise subprocess.CalledProcessError(return_code, 'stdOutLoop.py')

for path in execute(['python','-u',  'stdOutLoop.py']):
	print path,

#stdout = process.communicate()[0]

#while process.poll() is None:
#	l = process.stdout.readline()
#	print l
#	sys.stdout.flush()
#process.stdout.close()
#print process.stdout.read()

#for line in iter(process.stdout.readline, ''):
#	print line
