#Booleans are either True or False
#NUMBERS can be integers, floats, fractions or even complex numbers
#STRINGS are sequences of Unicode characters
#BYTES and byte arrays
#LISTS are ordered sequences of values
#TUPLES are ordered, immutable sequences of values
#SETS are unordered bags of values
#DICTIONARIES are unordered bags of key-value pairs

'''
EVERYTHING IS AN OBJECT!

'''
#legacy issues: booleans can be treated as numbers LOL.
"True + True"
True + True #equals 2
"True - False"
True - False # 1
"True * False"
True * False # 0
"True / False"

'''
COERCING INTEGERS TO FLOATS AND VICE-VERSA

'''

float(2)
int(2.0)
int(2.5)
int(-2.5)
1.12345678901234567890
type(10000000000000000)


'''
NUMBERS IN A BOOLEAN CONTEXT

'''

def is_it_true(anything):
	if anything:
		print("yes, it's true")
	else:
		print("no, it's false")
is_it_true(1)
is_it_true(0)
is_it_true(0.0)
