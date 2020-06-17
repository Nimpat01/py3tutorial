'''Q) What is Function
   A) A Function is a block of code which is reusable 
   to perform same operation'''
#Lets define function which create fibonacci series
#Here num is number of fibonacci element given as output of this function
#0 1 1 2
def fibonacci_num(num):
	a=0
	b=1
	fibonacci=[]
	fibonacci.append(0)
	fibonacci.append(1)
	if(num>1):
		for i in range (2,num):
			fibonacci.append(a+b)
			a=b
			b=fibonacci[i]
	print(fibonacci)	

fibonacci_num(50)