import json

'''
# to read json data
fo=open("/home/avi/Desktop/python/read_json_file.json")
data=json.load(fo)
print(data)
fo.close
'''

# to write to json file
my_json_data = {"name": "Avinash", "class": 12}
fo = open("/home/avi/Desktop/python/write_to_json_file.json", 'w')
json.dump(my_json_data, fo, indent=2)
fo.close()
