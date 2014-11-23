logfile = open('test.log', 'w')
logfile.write('test succeeded')
logfile.close()
print file('test.log').read()
logfile = open('test.log', 'a')
logfile.close()
print file('test.log').read()
test succeeded