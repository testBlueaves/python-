import json
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr
	
	def display(self):
		print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
	
e = Employee(100,"Ashish",90000,"patiala")
emp_dict = e.__dict__
print(emp_dict)
# serialization
with open('emp.json','w') as f:
	json.dump(emp_dict,f,indent=4)

# deserialization
with open('emp.json','r') as f:
	d= json.load(f)
print(type(d))
newemp = Employee(d['eno'],d['ename'],d['esal'],d['eaddr'])

newemp.display()
