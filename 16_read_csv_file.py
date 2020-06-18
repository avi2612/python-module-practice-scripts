# reading csv file without csv module

'''
file_path="/home/avi/Desktop/python/IAM.csv"
open_csv=open(file_path,'r')
data=open_csv.readlines()
open_csv.close()

for each in data:
    print(each.strip('\n').split(','))
'''


# reading file with help of csv module
'''
import csv
file_path = "/home/avi/Desktop/python/IAM.csv"
open_csv = open(file_path, 'r')
data = csv.reader(open_csv)
for each in data:
    print(each)
open_csv.close()
'''

'''
# finding length of csv file
import csv
file_path = "/home/avi/Desktop/python/IAM.csv"
open_csv = open(file_path, 'r')
print(f"csv have {len(list(csv.reader(open_csv)))-1} no of lines")
open_csv.close()
'''

# printing header of csv file
import csv
file_path = "/home/avi/Desktop/python/IAM.csv"
open_csv = open(file_path, 'r')
print(next(csv.reader(open_csv)))
open_csv.close()