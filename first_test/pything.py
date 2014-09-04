#currently this code will rename itself if given only one argument. I wonder why that is the case.


#maybe we can start with a file renaming thing
import os, sys
from sys import argv
##too many arguments, how do i fix this?
script, first, second = argv

print("the script is called:", (script))
print("your first variable is:", (first))
print("your second variable is:", (second))

# list the director
print "The dir has: %s"%os.listdir(os.getcwd())

refile = raw_input('hello world, what file do you want to rename?')
newfile = raw_input('what should we name it to?')


# renaming directory ''tutorialsdir"
#os.rename("tutorialsdir","tutorialsdirectory")

# renaming file "aa1.txt"
os.renames(refile, newfile)

print "File(s) successfully renamed. The dir now has: %s"%os.listdir(os.getcwd())