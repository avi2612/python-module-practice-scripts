import os
import platform
import sys

file_name=input("Enter your filename ")
if not (file_name):
    print("Enter your filename ")
    sys.exit()
if platform.system() == 'Linux':
    for path,directorys,files in os.walk('/'):
        for each in files:
            if file_name == each:
                print(os.path.join(path,file_name))
    sys.exit()

elif platform.system() == 'Windows':
    import string
    for drive in string.ascii_uppercase:
        if os.path.exists(drive+":\\"):
            for path,directorys,files in os.walk(drive+':\\'):
                for each in files:
                    if file_name == each:
                        print(os.path.join(path,file_name))
    sys.exit()

else:
    print("Unknown Operating System")
