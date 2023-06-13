# encode() -> To convert an object to json_string
# decode() -> To convert json_string to orignal object
# pip install jsonpickle
import json
import jsonpickle
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr
	
	def display(self):
		print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
	
e = Employee(100,"ashish",100000.00,"patiala")

# serialization
json_string = jsonpickle.encode(e)
print(json_string)

# serialization with file
with open('empkl.json','w') as f:
	f.write(json_string)

# deserialization
newemp = jsonpickle.decode(json_string)
newemp.display()

# deserialization from file
with open('empkl.json','r') as f:
	json_string = f.readline()
newe = jsonpickle.decode(json_string)
newe.display()