# read from file

'''
## file content as string
open_file_cursor_object1=open("/home/avi/Desktop/python/my_text_file_read.txt")
data1=open_file_cursor_object1.read()
open_file_cursor_object1.close()
print(data1)
'''

'''
## file content as list
open_file_cursor_object2=open("/home/avi/Desktop/python/my_text_file_read.txt")
data2=open_file_cursor_object2.readlines()
open_file_cursor_object2.close()
for each_line in data2:
    print(each_line)
# print last line, print(data2[-1])
'''

# write to file

'''
# wring single file
write_file_cursor_object1=open("/home/avi/Desktop/python/my_text_file_read.txt",'w')
data1=write_file_cursor_object1.write('hello bhai happy birthday\n')
write_file_cursor_object1.close()
'''

'''
# wring multiple lines from list
my_data=['1. avi\n','2. alok\n','3. sourabh\n']
write_file_cursor_object2=open("/home/avi/Desktop/python/my_text_file_read.txt",'w')
data2=write_file_cursor_object2.writelines(my_data)
write_file_cursor_object2.close()
'''

# writing multiple file best way
write_data_cursor_object3=open("/home/avi/Desktop/python/my_text_file_read.txt",'w')
for i in range(5):
    write_data_cursor_object3.write(f"this is line no {i}\n")
    i += 1
write_data_cursor_object3.close()



# append to file, file should be present

write_data_cursor_object3=open("/home/avi/Desktop/python/my_text_file_read.txt",'a')
for i in range(5):
    write_data_cursor_object3.write(f"this is line no {i}\n")
    i += 1
write_data_cursor_object3.close()