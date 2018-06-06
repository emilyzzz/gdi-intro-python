# to help understand which line is executed and in what order

print('Line 3')

def func1():
   print('Begin func1')


def func2():
   print('Begin func2')
   return

def func3(x):
   print('Begin func3, input is: ', x)
   func1()
   func2()
   print('End func3')


print('Before calling func3...')
func3(10)
print('After calling func3...')
