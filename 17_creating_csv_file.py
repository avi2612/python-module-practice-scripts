import csv
file_path = "/home/avi/Desktop/python/write_to_csv_file.csv"

write_to_file = open(file_path, 'w')

write_in_csv_file = csv.writer(write_to_file, delimiter=",")

write_in_csv_file.writerow(["S.No", "Name", "Age"])
write_in_csv_file.writerow(["1", "Avinash", 21])
write_in_csv_file.writerow(["2", "Alok", 26])
write_in_csv_file.writerows([["2", "Alok", 26],["24", "Alok", 246],["2", "Alolll", 26]])


write_to_file.close
