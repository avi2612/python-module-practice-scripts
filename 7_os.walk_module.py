import os

path="/home/avi/temp"

# print(list(os.walk(path)))

for path_directory,directory,files in os.walk(path):
    if (files):
        for each in files:
            print(os.path.join(path_directory,each))