#Tuple is sequence data type. Tuple is consist of number of values separated by commas
#Tuple is immutable object with heterogeneous seqence of element.
#Tuple can be accessed by unpacking and indexing method.
#What is immutable?
#>> Object which can be modified is Immutable. immutable object contains Number string and tuple.

programming_languages = "Python", "JAVA", "C++", "C#"
hdl = "Verilog", "VHDL", "SystemVerilog"
# For Loop, variable for that loop and Tuple
# Here language is same as "i" we use in C language
# Type of programming_languages
print(type(programming_languages))
for language in programming_languages:
    print(language)
print(type(hdl))    
for HDL in hdl:
    print(HDL)

#calling Tuple into tuple

all_language_i_know = programming_languages, hdl
print(type(all_language_i_know))
print(all_language_i_know)
for language in all_language_i_know:
    for i in language:
        print(i)
#how to construct tuple with single or zero value?

#Tuple with zero value

empty =()
print (type(empty))

#Tuple with sigle value

MyName = "Nimesh",
print(type(MyName))
#When you print this then it will print in parantheses which means its tuple 
print(MyName)
for NAME in MyName:
    print(NAME)
#print (len (hdl))    

x,y,z = hdl
#print(x)
#print(y)
#print(z)
j=len(hdl)
i_want_to_code_in = {}   
for i in range(0,len(hdl)):
    j=j-1
    i_want_to_code_in[j]=hdl[i]
print(type(i_want_to_code_in))    
print(i_want_to_code_in)    