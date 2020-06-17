'''Q) What is Function
   A) A Function is a block of code which is reusable 
   to perform same operation
   The keyword 'def' introduces a function defination'''
'''The global statement
   The global statement is a declaration which holds for the entire current code block. 
   It means that the listed identifiers are to be interpreted as globals.
   It would be impossible to assign to a global variable without global.
   Free variables may refer to globals without being declared global.
   The nonlocal statement
   The nonlocal statement causes the listed identifiers to refer to previously bound 
   variables in the nearest enclosing scope excluding globals.
   This is important because the default behavior for binding is to search the local namespace first.'''
#Lets define function which create fibonacci series
#Here num is number of fibonacci element given as output of this function

def fibonacci_num(num):
	'''This function will print "num" fibonacci element of fibonacci series '''
	fibonacci=[]
	if(num==1):
		fibonacci.append(0)
		print(fibonacci)
	elif(num==2):
		fibonacci.append(0)
		fibonacci.append(1)
		print(fibonacci)			
	elif(num>2):
		a=0
		b=1
		fibonacci.append(0)
		fibonacci.append(1)
		for i in range (2,num):
			fibonacci.append(a+b)
			a=b
			b=fibonacci[i]
		print(fibonacci)			
	else:
		print("Wrong parameter")		


fibonacci_num(0)
fibonacci_num(50)