# program to check java version using subprocess module

import subprocess
import sys

cmd='java -version'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ,universal_newlines=True)
rc=sp.wait()
output, error=sp.communicate()

#print(rc)
#print(output)
#print(error)

if rc != 0:
    print(f"please check your command again, it failed with err => {error} \n {rc}")
else:
    if bool(output)==False and bool(error)==True:
       print(error[17:26])
