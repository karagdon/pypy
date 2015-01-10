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