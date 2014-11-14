from calculator import *

if add(1,1) != 2:
    print "add(1,1) failed!"

if add(0,1) != 1:
    print "add(0,1) failed!"

if add(100,100) != 200:
    print "add(100,100) failed!"

if add(-1,1) != 0:
    print "add(-1,1) failed!"

print "Tests all done!"
