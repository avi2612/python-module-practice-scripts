# checking bash version using subprocess module

import subprocess
import sys

# cmd='cat /etc/os-release' # when shell is true
# cmd='ls -ltr /home/avi/'
# cmd=['cat', '/etc/os-releause']
# cmd=['cat', '/etc/os-release']
cmd='bash --version'

sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ,universal_newlines=True)
rc=sp.wait()
output, error=sp.communicate()
if rc != 0:
    print(f"please check your command again, it failed with err => {error}")
    sys.exit()

for i in output.splitlines():
    print(i[18:27])
    sys.exit()