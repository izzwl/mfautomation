import subprocess
import thread
from time import sleep
proses = subprocess.Popen("x3270if -t 6000 \"transfer(hostfile=mpmcs99.transfer,localfile=IVR4025,exist=replace,buffersize=4096)\"",shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

proses.communicate()

while True:
	sleep(1)
	#print(proses.poll())
	#print(proses.stdin)
	print(proses.stdout)
	#print(proses.stderr)
	#print(proses.returncode)
