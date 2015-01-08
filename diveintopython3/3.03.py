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

# dictionary comprehensions
metadata_dict = {f:os.stat(f) for f in glob.glob('*test*.py')}  ③
 
# this is NOT dictionary comprehension
metadata = [(f, os.stat(f)) for f in glob.glob('*test*.py')]
metadata[0]