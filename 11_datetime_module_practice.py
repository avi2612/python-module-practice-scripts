# python program to print all files which are older than x days

import sys
import datetime
import os

my_path = input("What is the path you want to scan for older files => ")
older_days = 30
result=[]

if not os.path.exists(my_path):
    print("Enter again this is not a valid path")
    sys.exit(1)
if os.path.isfile(my_path):
    print("Enter again this is not a valid directory path")
    sys.exit(2)

if len(os.listdir(my_path)) == '0':
    print("Given path is Empty ")

today = datetime.datetime.now()
for each_file in os.listdir(my_path):
    modified_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(my_path, each_file)))
    age = (today-modified_time).days
    if age > older_days:
        result.append(os.path.join(my_path, each_file))

print(f"\nFound total {len(result)} results\n")
l=1
for each in result:
    print(l,each)
    l += 1