#user input
import sys
from sys import argv
movie_dict = {}
title = argv[1]
genres = str(argv[2:])

#read the file
with open('movies.txt','r', encoding='utf-8') as movieFile:
    movies_dict = eval(movieFile.read())
type(movies_dict.values())
movies_dict[title] = genres

for key, values in movies_dict.items():
	print (key + "\t: " + str(values).strip('[\']'))
	
	
#print (', '.join(movies_dict.values()))


#	print (k + "\t : " +  str(movies_dict[k]).strip('[]'))
	
"""
# check if is in dict
if title in movies_dict:
	print ("Not added. That movie already exists, use -e to edit the movie")
	pass

#write to the file
else:
	with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
		movieFile.write(str(movies_dict))
		print ("add complete")
"""