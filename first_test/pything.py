#starting new code
print "hello world"

#maybe we can start with a file renaming thing
import os, sys

# listing directories
print "The dir is: %s"%os.listdir(os.getcwd())

# renaming directory ''tutorialsdir"
os.rename("tutorialsdir","tutorialsdirectory")

# renaming file "aa1.txt"
os.renames("aa1.txt","newdir/aanew.txt")