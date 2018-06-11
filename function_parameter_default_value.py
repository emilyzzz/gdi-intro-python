"""
Description
    Below, I'm using a immutable variables 'message' and 'n', and mutable 'values', to pass to function 'log1'.

    Mutable variables are suggested to default to immutable values, otherwise unexpected result may happen.
    This is a common 'gotcha' in Python.
    http://docs.python-guide.org/en/latest/writing/gotchas/
    The 'log2' below is using this BAD pattern. 'log1' below is using the SUGGESTED pattern.

Objective
    1. Be aware of the 'common gotcha' in Python. It's suggested to default to None in list/dict func argument.
    2. "Positional argument" and "keyword argument"
    3. we can't pass keyword argument in front of positional args. invalid syntax
"""


def log2(message, n=0., values=[]):                  # 'values' defaults to mutable list, CAUTION!
    print("\tInput n =", n)
    print("\tInput message =", message)
    print("\tInput values =", values)


def log1(message, n=0., values=None):                # 0. is same as 0.0,  5. == 5.0
    if values is None:
        values = []
    print("\tInput n =", n)
    print("\tInput message =", message)
    print("\tInput values =", values, '\n')

print('1.1, calling function with all inputs')
log1('My numbers are', 1.1, [1, 2])
log1('Hi there', 1.1, [])

print('1.2, calling function using keyword arguments')
log1(message='My numbers are', n=1.2)
log1(message='Hi there', values=[1,2])

print('1.3, calling function with only required input...')
log1("My numbers are")
log1("Hi there")

print('1.4, calling function with keyword arg for requirex input...')
log1(message="My numbers are")
log1(message="Hi there")


# Python will raise: SyntaxError: positional argument follows keyword argument, uncomment to see the error
print('1.5, invalid syntax: keyword arg in front of positional arg...')
#log1(message="My numbers are", 1.5)     # '1.5' is positional arg, 'message' is keyword arg.



