import json
class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr
	
	def display(self):
		print(f'eno:{self.eno} ename: {self.ename} esal: {self.esal} eaddr: {self.eaddr}')
	