# program to list all particular type of file in specific directory

import os
import sys

my_path = input("Enter your path => ")
if os.path.exists(my_path):
    if not os.listdir(my_path):
        print("given path is empty")
        sys.exit()
else:
    print("path is invalid")
    sys.exit()

extension = input("Enter extension of file you want to file , like .py .mp4 => ")
found = []
for each in os.listdir(my_path):
    if each.endswith(extension):
        found.append(each)
print(f"\n found total {len(found)} results\n")
count = 1
for result in found:
    print(count,os.path.join(my_path, result))
    count += 1