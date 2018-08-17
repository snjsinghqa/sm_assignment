import json

with open('data_json.txt') as file:
    data = json.load(file)
    for p in data['people']:
        print("Employee Name: "+ p['Name'])
        print("Employee Department: "+ p['Department'])
        print("Employee Address: " + p['From'])
        print('')

