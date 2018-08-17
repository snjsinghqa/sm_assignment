import json

data = {}
data['people'] = []
data['people'].append({'Name': 'Sanjay',
                       'Department': 'QA',
                       'From': 'Indore'})
data['people'].append({'Name': 'Mohit',
                        'Department': 'Dev',
                        'From': 'Bhopal'})
data['people'].append({'Name': 'Rohit',
                       'Department': 'Admin',
                       'From': 'Delhi'})
data['people'].append({'Name': 'Jackson',
                       'Department': 'Tech',
                       'From': 'USA'})
data['people'].append({'Name': 'John',
                       'Department': 'Support Team',
                       'From': 'UK'})
with open('data_json.txt','w') as write_data:
    json.dump(data,write_data)
