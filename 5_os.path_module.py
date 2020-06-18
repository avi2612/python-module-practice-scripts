import os

# print(os.path)
# print(dir(os.path))
path1="/home/avi/temp/tt/password_category.js"
path2="/home/avi/temp/tt/"
path3="avi.txt"

print(os.path.exists(path1))
print(os.path.isfile(path1))
print(os.path.isdir(path2))
print(os.path.islink(path2))
print(os.path.basename(path1))
print(os.path.dirname(path1))
print(os.path.join(path1,path3))
print(os.path.split(path1))
print(os.path.getsize(path1))


