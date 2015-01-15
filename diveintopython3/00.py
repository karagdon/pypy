# take input (genre)
# create a structure that stores a movie title with multiple genres
# return titles with genre

#use python to create an XML document that stores information

import xml.etree.ElementTree as etree
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed', attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print(etree.tostring(new_feed))