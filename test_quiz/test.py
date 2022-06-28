q1 = 'What is a correct syntax to output "Hello World" in Python?'
option1 = ['echo("Hello World")','p("Hello World")','echo"Hello World"','print("Hello World")']

q2 = 'How do you insert COMMENTS in Python code?'
option2 = ['#This is s comment','//This is s comment','/*This is s comment*/']

q3 = 'Which one is NOT a legal variable name?'
option3 = ['Myvar','my-var','_myvar','my_var']

q3 = 'How do you create a variable with the numeric value 5?'
option3 = ['x=int(5)','x=5','Both the other answers are correct']

option = [option1,option2,option3]
ans = ['print("Hello World")','#This is s comment','my-var','Both the other answers are correct']

o = ['a','b','c','d']
questions = [q1,q2,q3]
print()
j=0
for x in questions:
	
	print(' '+x)
	i=0
	for op in option[j]:
		print('  ',o[i]+')',op)
		i+=1
	print()
	n = input('Select your ans : ')
	if n not in o:
		print('Wrong option Please select a,b,c,d!!!!!!')
	else:
		if option[j][o.index(n)] in ans:
			print("----Correct ----\n")
		else:
			print("----Not Correct----\n")
		#print(o.index(n))

	j+=1
