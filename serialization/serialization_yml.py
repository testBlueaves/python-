# YAML Ain't Markup Language 
# Yet Another Markup Language
# more readable and ligt weight then json

from pyaml import yaml

emp_dict  = {
    'Person 1': {'age': 20, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']},
    'Person 2': {'age': 21, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']},
    'Person 3': {'age': 22, 'city': 'New York', 'hobbies': ['reading', 'hiking', 'coding']}
}





# serialization from dict object to yaml string
yaml_string = yaml.dump(emp_dict)
print(yaml_string)

# dump() to serialize from python dict object to yaml string/file
# serialization to yaml file
with open('emp.yaml','w') as f:
	yaml.dump(emp_dict,f)

# Deserilaization from yaml string to python dict
ed = yaml.safe_load(yaml_string)
for k,v in ed.items():
	print(f'{k} --> {v}')

# Deserialization from yaml file
with open('emp.yaml','r') as f:
	ed2 = yaml.safe_load(f)
	print(ed2)
print(type(ed2))
print(ed2)
