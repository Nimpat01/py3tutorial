#This quiz is for mutable and unmutable variable type
#This explain about Global and local variable

#In this X is Immutable 	
x = 1
def test():
    x = 2
test()
print(x)

#In this X becaome global in function hence it will reflect same value after function
x = 1
def test():
    global x
    x = 2
test()
print(x)

#X is local list 
x = [1]
def test():
    x = [2]
test()
print(x)

#X become global list
x = [1]
def test():
    global x
    x = [2]
test()
print(x)

#x is list which etry can be modified
x = [1]
def test():
    x[0] = 2
test()
print(x)