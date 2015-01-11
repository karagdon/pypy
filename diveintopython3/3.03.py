a_list = [1, 9, 8, 4]
a_list = [elem * 2 for elem in a_list]
print (a_list)


import os, glob
glob.glob('*.xml')
[os.path.realpath(f) for f in glob.glob('*.xml')
[os.path.realpath(f) for f in glob.glob('*.xml')]
# This returns a list of all the .xml files in the current working directory.

[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.xml')]
#	This list comprehension finds all the .xml files in the current working directory, gets the size of each file (by calling the os.stat() function), and constructs a tuple of the file size and the absolute path of each file (by calling the os.path.realpath() function).

# A dictionary comprehension is like a list comprehension, but it constructs a dictionary instead of a list.
# dictionary comprehensions
metadata_dict = {f:os.stat(f) for f in glob.glob('*test*.py')}  ③
 
# this is NOT dictionary comprehension
metadata = [(f, os.stat(f)) for f in glob.glob('*test*.py')]

metadata[0]

metadata_dict = {f:os.stat(f) for f in glob.glob('*')}
humansize_dict = {os.path.splitext(f)[0]:humansize.approximate_size(meta.st_size)
				for f, meta in metadata_dict.items() if meta.st_size > 6000}
list(humansize_dict.keys())

a_dict = {'a': 1, 'b': 2, 'c': 3}
{value:key for key, value in a_dict.items()}

# SET COMPREHENSIONS
a_set = set(range(10))
{x for x in a_set if x % 2 == 0}
{2**x for x in range(10)}
#Set comprehensions do not need to take a set as input; they can take any sequence.

#some practice
>>> a_set = set(range(5))
>>> a_set
{0, 1, 2, 3, 4}
>>> {(x**2)/2 for x in range(5)}
{0.0, 0.5, 2.0, 8.0, 4.5}
>>> {x+"set modified" for x in range(5)}
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 1, in <setcomp>
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> {x+"a" for x in range(5)}
#Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "<stdin>", line 1, in <setcomp>
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> {x+2 for x in range(5)}
{2, 3, 4, 5, 6}
>>> {"set item" for x in range(5)}
{'set item'}

>>> {str(x) for x in range(5)}
{'2', '0', '3', '4', '1'}
>>> {str(x)+"set item is now a string \n" for x in range(5)}
{'4set item is now a string \n', '0set item is now a string \n', '1set item is now a string \n', '2set item is now a string \n', '3set item is now a string \n'}