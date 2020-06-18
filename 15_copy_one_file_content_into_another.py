import os
import sys

source = input("Enter source file path => ")
if not os.path.exists(source):
    print("check again, entered source path is invalid")
    sys.exit()
if os.path.isdir(source):
    print("check again, entered source path is invalid")
    sys.exit()

destination = input("Enter destination file path => ")

file_read_object = open(source, 'r')
data = file_read_object.read()
file_read_object.close()

file_write_object = open(destination, 'w')
file_write_object.write(data)
file_write_object.close()
