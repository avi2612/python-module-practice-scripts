# sys module program based on argv

import sys

'''
print(sys.version)
print(f"script name and path is '{sys.argv[0]}'")
print(sys.path)
'''


if len(sys.argv) != 3:
    print("please pass two command line input ,    'text'    ,   action =>    'upper | lower'")
    sys.exit()
if sys.argv[2] == "upper":
    print(sys.argv[1].upper())
elif sys.argv[2] == "lower":
    print(sys.argv[1].lower())
else:
    print("please check your input")