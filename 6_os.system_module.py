import os
import platform

print(os.system('uname'))
# success => 0

'''
print(os.system('unamel'))
a=os.system('apt-get update')
print(a)
'''
if platform.system()=="Linux":
    os.system('clear')
elif platform.system()=='Windows':
    os.system('cls')
else:
    print("Unknown os")