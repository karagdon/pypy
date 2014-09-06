#currently this code will rename itself if given only one argument. I wonder why that is the case.


import os, sys
from sys import argv
script, refile, newfile = argv

if os.path.exists(refile):
  print "%s ---> %s, Success!" % (refile,newfile)
  os.renames(refile, newfile)
  print "File(s) successfully renamed. The dir now has: %s"%os.listdir(os.getcwd())
  
else:
  print "%s doesn't exist"%refile