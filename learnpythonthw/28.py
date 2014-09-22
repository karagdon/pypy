Python 2.7.3 (default, Feb 27 2014, 19:58:35)
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> True and True
True
>>> False and True
False
>>> 1 == 1 and 2 == 1
False
>>> True and 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> False and 0 != 0
False
>>> True or 1 == 1
True
>>> "test" ! == "testing"
  File "<stdin>", line 1
    "test" ! == "testing"
           ^
SyntaxError: invalid syntax
>>> "test" != "testing"
True
>>> "test" == 1
False
>>> not (True and False)
True
>>> not (1 == 1 and 0 != 1)
False
>>> not (10 == 1 or 1000 == 1000)
False
>>> not (1 == 1  and 0 != 1)
False
>>> not (1 != 10 or 3 == 4)
False
>>> not ("testing" = "testing" and "Zed == "Cool Guy"
  File "<stdin>", line 1
    not ("testing" = "testing" and "Zed == "Cool Guy"
                   ^
SyntaxError: invalid syntax
>>> not ("testing" == "testing" and "Zed == "Cool Guy")
  File "<stdin>", line 1
    not ("testing" == "testing" and "Zed == "Cool Guy")
                                                ^
SyntaxError: invalid syntax
>>> not ("testing" == "testing" and "Zed"  == "Cool Guy")
True
>>> 1 == 1 and (not ("testing" == 1 or 1 == 0))
True
>>> "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
False
>>> 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
False