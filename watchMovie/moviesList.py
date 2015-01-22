import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-a", "--addMovie", action="customActiontoAdd", dest = "add", help="adds Movie")
parser.add_argument("-e", "--editMovie", action="customActiontoEdit", dest = "edit", help="edits Movie")
parser.add_argument("-rm", "--removeMovie", action="customActiontoRemove", dest = "remove", help="removes Movie")
parser.add_argument("-w", "--watched", action="customActiontoMarkWatched", dest = "watched", help="mark Movie as watched")

args = parser.parse_args()

##destination ( dest = "add") to function
"""
movies_dict[title] = genres
def add():

#def edit():
	# check if is in dict
	if title in movies_dict:
		with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
		movieFile.write(str(movies_dict))
		print ("edit complete")
	else:
		print ("DNE")
		pass
	

#def remove():
	# check if is in dict
	if title in movies_dict:
		del movies_dict[title]
		with open('movies.txt', mode='w', encoding='utf-8') as movieFile:
		movieFile.write(str(movies_dict))
		print ("deleted {title}, complete")
	else:
		print ("DNE")
		pass
	
#def watched()
watched = 'watched'
if watched in movies_dict:
	pass
else:
	movies_dict[title].append(watched)

"""