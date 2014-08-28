#starting new code


#maybe we can start with a file renaming thing
import os, sys
from sys import argv
refile, newfile = argv

# list the director
print "The dir has: %s"%os.listdir(os.getcwd())

# refile = raw_input('hello world, what file do you want to rename?')
# newfile = raw_input('what should we name it to?')


# renaming directory ''tutorialsdir"
#os.rename("tutorialsdir","tutorialsdirectory")

# renaming file "aa1.txt"
os.renames(refile, newfile)

print "File(s) successfully renamed. The dir now has: %s"%os.listdir(os.getcwd())