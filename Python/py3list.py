#What is list?
#List is compound data type.
#list can be written as list of value separedted by commas in suare bracket.
#List might contain different type of item, but usually items have same data type.

#Like all other sequence type List can be sliced and indexed
fibbonaci_sequence = [0, 1, 1, 2, 3, 5]

print(type(fibbonaci_sequence))
print(fibbonaci_sequence)
#List            = [0, 1, 1, 2, 3, 5]
#Positive index  =  0  1  2  3  4  5
#Negative index  = -6 -5 -4 -3 -2 -1
print(fibbonaci_sequence[-1])

#Slicing retunr new list
#Here left limit is inclusive where as right limit is exclusive
#In below entry it will exclude 4th entry
first_4_fibbonaci_sequence = fibbonaci_sequence[:4]
print(first_4_fibbonaci_sequence)

#Shallow Copy of list
Shallow_copy_of_fibbonaci_sequence = fibbonaci_sequence[:]
print(Shallow_copy_of_fibbonaci_sequence)

#List also support operation like concatenation

fibbonaci_sequence = fibbonaci_sequence + [8, 13, 21, 34, 55]
print("type of fibbonaci_sequence")
print(type(fibbonaci_sequence))
print("fibbonaci_sequence after concatenation")
print(fibbonaci_sequence)

#List are mutable type

print("Printing 5th value of fibbonaci_sequence")
print(fibbonaci_sequence[5])
print("Updating fibbonaci_sequence's 5th value")
fibbonaci_sequence[5] = 1000
print("Printing fibbonaci_sequence's type")
print(type(fibbonaci_sequence))
print("Printing fibbonaci_sequence")
print(fibbonaci_sequence)

fibbonaci_sequence[5] = 5
#Adding more entry is possing in list by using append() 
fibbonaci_sequence.append(89)
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

Shallow_copy_of_fibbonaci_sequence = fibbonaci_sequence[:]
# With list assignmet to silce is also possible

fibbonaci_sequence[3:6] = [0, 0 ,0]
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

fibbonaci_sequence[3:6]= [2, 3, 5]
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

#if right hand side list size is not same as slice then it will shift list value.
#here also right side limit is exclusive 

fibbonaci_sequence[3:5] = [0, 0 ,0]
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

fibbonaci_sequence[3:5]= [2, 3, 5]
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

fibbonaci_sequence=Shallow_copy_of_fibbonaci_sequence
print(type(fibbonaci_sequence))
print(fibbonaci_sequence)

#length of List by using built in function len
print("length of fibbonaci_sequence:",len(fibbonaci_sequence))

#It is possible to nest lists 

N1 = ['a','b','c']
N2 = [1  , 2 , 3 ]
N3 = ["Python", "Verilog"]

N = [N1, N2, N3]
print(type(N))
print(N)
print(N[0][2])
print(N[2][1]) 

N1.append('d')
print(N1)
N1[len(N1):]='e'
print(N1)

#iterable

A = [ 0 , 1 , 1 , 1, 2 , 3 , 4 , 4 , 5]
print(A)
A.extend('6')
print(A)

#insert
A.insert(len(A),7)
print("After inserting 7 at last location")
print(A)

#remove
A.remove('6')
print("Removing '6' from list A")
print(A)

#pop
A.pop((len(A)-1))
print("Removing last entry in list A")
print(A)

A_bkup = A[:]

#clear
A.clear()
print("Clearing list A")
print(type(A))
print(A)

A = A_bkup
A_bkup = A[:]
print(A)
#Clearing array is euivalent to del A
#del A[:] will delet shallow copy of A as well
del A[:]
print("Deleting entry in list A")
print(type(A))

A = A_bkup
print(A)
#Index
print("Printing index for entry 4")
print(A.index(4))

#count
print(A)
print("Printing number of time 7 appear in list A")
print(A.count(7))
print("Printing number of time 3 appear in list A")
print(A.count(3))

#reverse

print(A)
A.reverse()
print(A)

#using list as stack
#Beacuse of above explained List's method its easy to use List as stack.
#Where last element added and first element retrieved
#last-in,First-out
#use list.append() to add value
#use list.pop to retrieve value 

stack_a = [1, 2, 3]
print(stack_a)
stack_a.append(4)
print(stack_a)
stack_a.append(5)
print(stack_a)
stack_a.pop(0)
print(stack_a)
stack_a.pop(0)
print(stack_a)






















