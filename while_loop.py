# the code below will calculate the factorial of a positive numbr


input_value = input('Enter a positive integer:')
n = int(input_value)                           # use "eval" or "int" to convert string to integer
result = 1

while n > 1:
    result = result * n                         # assign right to left
    n = n - 1                                   # whole 'while block' indented

print("The factorial of {0} is: {1}".format(input_value, result))          # 'format' function
