"""
Practice for Lecture 1:
1. create python file change_counter.py from terminal or in PyCharm
2. use 'input()' function to prompt user to input how many quarters, example on python shell:
3. Write code in a text editor, prompt users to input number of: quarters, dimes, nickels, pennies,
   and save the four numbers in four variables
4. Run code from terminal:  python3 change_counter.py
5. Calculate the total amount we have in cents, using arithmetic operators like: +,  *
6. Print to screen: "Total amount of money is: xxx cents",  please use old style string formatting
7. Print to screen: "Total amount of money is: x.xx dollars", keep 2 decimal places, using old style formatting
"""

# 'input' built-in function will return string type of number, for example '100',
# to get the 'int' type, use 'eval' built-in function, that converts string -> number (int or float)
quarters = input('Please input how many quarters: ')
quarters = eval(quarters)

# having 2 functions (eval, input) on same line, is equivalent as in separate lines above
dimes = eval(input('Please input how many dimes: '))
nickels = eval(input('Please input how many nickels: '))
pennies = eval(input('Please input how many pennies: '))

total = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1

# old style python string formatting
print('Total amount of money is: %s cents' % total)

# new style python string formatting
print('Total amount of money is: {} dollars'.format(total/100))
