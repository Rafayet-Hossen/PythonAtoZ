import json
data = {
    "name" : "John Doe",
    "age" : 30,
    "city" : "Dhaka"
}

#json dumps() ==> convert data into json format

json_data = json.dumps(data)

print(type(json_data)) #this will be a string
print(type(data)) #this will be a dict

dicts = json.loads(json_data)
print(type(dicts))
print(dicts['name'])