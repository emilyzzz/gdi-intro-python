var = 100                                     # executed line 1
if var == 200:                                # executed line 2
   print("1 - Got a true expression value")   # 'print' to debug
   print("var == 200\n")
elif var == 150:                              # executed line 3
   print("2 - Got a true expression value")
   print("var == 150\n")
elif var == 100:                              # executed line 4
   print("3 - Got a true expression value")   # executed line 5
   print("var == 100\n")                      # executed line 6
else:
   print("4 - Got a false expression value")
   print("var=%s\n" % var)

print("Good bye!\n")     # always execute since it's out of 'if'
