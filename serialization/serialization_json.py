#-------------------deserialization-----------------
# loads() --> Converting JSON string to python dict
# load() --> Reading json from a file and conveting that json into python dict 

#-------------------serialization-------------------
# dunp() --> from python dict to json and write json to file
# dumps() --> from pyhton dict to json string

import json
employee = {
'name':'ashish',
'age':25,
'salary':25000.00,
'isMarried':False,
'girlFriend':True,
'ex':None
}

# serialization from python dict obj to json_string
json_string = json.dumps(employee,indent=4,sort_keys=True)
print(json_string)

# serialization from python dict object to json file

with open('emp.json','w') as f:
	json.dump(employee,f,indent=4)

# deserialization json_string to python dict
py_dict = json.loads(json_string)
print(py_dict)

with open('emp.json','r') as f:
	emp_dict = json.load(f)
print(emp_dict)

