
Type "help", "copyright", "credits" or "license" for more information.
>>> logfile = open('test.log', 'w')
>>> logfile.write('test succeeded')
>>> logfile.close()
>>> print file('test.log').read()
test succeeded
>>> logfile = open('test.log', 'a')
>>> logfile.close()
>>> print file('test.log.read()
  File "<stdin>", line 1
    print file('test.log.read()
                              ^
SyntaxError: EOL while scanning string literal
>>> print file('test.log).read()
  File "<stdin>", line 1
    print file('test.log).read()
                               ^
SyntaxError: EOL while scanning string literal
>>> print file('test.log').read()
test succeeded