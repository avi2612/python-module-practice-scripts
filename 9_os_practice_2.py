# os module script to list files and directory in particular folder and specifying its type

import os
import sys
my_path=input("Enter your path to list files and folder => ")
if os.path.exists(my_path):
    if os.path.isdir(my_path):
        files=os.listdir(my_path)
    else:
        print("this is file path not directory path")
        sys.exit()
else:
    print('entered path is not valid')
    sys.exit()

for each in files:
    if os.path.isdir(os.path.join(my_path,each)):
        print(os.path.join(my_path,each),'is directory')
    elif os.path.isfile(os.path.join(my_path,each)):
        print(os.path.join(my_path,each),'is file')
    elif os.path.islink(os.path.join(my_path,each)):
        print(os.path.join(my_path,each),'is link')
    else:
        print("chal jaa yaha se")

