#user input
import sys
from sys import argv
movie_dict = {}
title = argv[1]
genres = argv[2:]

#read the file
with open('movies.txt','r', encoding='utf-8') as movieFile:
    movies_dict = eval(movieFile.read())

movies_dict[title] = genres
# check if is in dict
if title in movies_dict:
	print ("Not added. That movie already exists, use -e to edit the movie")
	pass

#write to the file
else:
	with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
		movieFile.write(str(movies_dict))
		print ("add complete")