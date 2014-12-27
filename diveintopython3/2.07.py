# Dictionaries
# # /Unordered set of key-value pairs, optimized for retrieving value when you know the key
a_dict = {'server' : 'db.diveintopython3.org', 'database': 'mysql'}
a_dict['server']
a_dict['database']

#modifying
a_dict['database'] = 'blog'
a_dict['user'] = 'k8'
a_dict['user'] = 'day'
a_dict['user'] = 'k8day'

#mixed value dictionaries

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
			1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
			
len(SUFFIXES) #2
1000 in SUFFIXES #True
SUFFIXES[1000]
SUFFIXES[1000][3]
