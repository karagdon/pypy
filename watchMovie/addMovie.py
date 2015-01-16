#user input
import sys
from sys import argv
movie_dict = {}
title = argv[1]
genres = argv[2:]

#read the file
with open('movies.txt','r', encoding='utf-8') as movieFile:
    movies_dict = eval(movieFile.read())

#write to the file
movies_dict[title] = genres
with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
	movieFile.write(str(movies_dict))
