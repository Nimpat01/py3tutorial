#In this exercise will learn about Enumerate
#Enumerate
#->	Return an enumerate object
#->	enumerate(iterable, start=0)
#-> Now in above function argument iterable should be a seuence, 
#an iteratior or some object which support iteration
#-> enumerate returns a tuple containing count and 
#the values obtained from iterating over iterable.

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(type(seasons))
print(seasons)
print(list(enumerate(seasons)))
print(list(enumerate(seasons,start=1)))
seasons_with_month = [['Spring'	,'MAR'	,'APR' 	,'MAY'],
					  ['Summer'	,'JUN'	,'JULY'	,'AUG'],
					  ['Fall'	,'SEPT'	,'OCT' ,'NOV'],
					  ['Winter'	,'DEC'	,'JAN'	,'FAB']]
#print(seasons_with_month)
for count, x in enumerate(seasons_with_month):
	#for y in enumerate(x):
	print(count,x)

