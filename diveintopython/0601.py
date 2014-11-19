try:
	fsock = open("/notthere", "r")
except IOError:
    print "The file does not exist, exiting gracefully"
print "This line will always print"