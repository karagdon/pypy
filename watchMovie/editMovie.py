# check if is in dict
if title in movies_dict:
	with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
		movieFile.write(str(movies_dict))
		print ("add complete")


#write to the file
else:
	print ("Not added. That doesnt exist in the database, use -a to add the movie with genres")
	pass
