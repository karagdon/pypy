# take input (genre)
# create a structure that stores a movie title with multiple genres
# return titles with genre

#use python to create an XML document that stores information

#import xml.etree.ElementTree as etree
#new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', gattrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
#print(etree.tostring(new_feed))

#user input
import sys
from sys import argv
script, title, gen1, gen2, gen3, gen4, gen5 = argv

# how do i do this to have infinite genres
# how do i transform argv into an new isntance of an array


# This section takes the argv from above and takes the first element and makes it the title
#	to create a variable from string use vars()
#	goal: test = [1, 2, 3, 4, 5]
#	>>> foo="bar"
#	>>> vars()[foo] = 'qwertry'
#	>>> print bar  # --> 'qwertry'


# This will append the rest of the argvs into the elements of a new array
# [x, T, 1, 2, 3 , 4, 5]
newMovie = []

for eachArg in sys.argv[1:]:
    newMovie.append(str(eachArg))

print ("Title: " + newMovie[0])
print ("Genres :")
print (i for i[1:] in newMovie)

