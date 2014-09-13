from sys import argv

#this unpacks the argv and gets assigned to four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name = raw_input("What's your name?")
print name