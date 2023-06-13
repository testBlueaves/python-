import json
import pickle
from Employee import Employee

e = Employee(100,"ashish",1000.00,"punjab")

# serialaization of employee object
with open('emp.ser','wb') as f:
	pickle.dump(e,f)
	print('Object Serilaization Complete')

# Deserializarion of employee object
with open('emp.ser','rb') as f:
	emp = pickle.load(f)
	print('Oject Deserialization Complete')

print('printing Employee Information')
emp.display()