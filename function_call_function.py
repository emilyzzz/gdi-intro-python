"""
1. Function: inside of function, we can call other functions
2. String Formatting
    In this example, we introduce 4 different ways to do string formatting.
        a) use "+" sign to concatenate strings
        b) old style string formatting using %s, %f (for float)
        c) new style string formatting using str.format() function
        d) f string, new in python3.6
3. Global Variables
    a) valid as read-only throughout the code. Need extra step(google: python global variable) to edit their values.
    b) By convention, we define global variables on top of file, and use all capital letters.
    c) When code goes big, using global variables are discouraged since it may be modified unintentionally and
       lead to very hard to find bugs. The good use case is some constants that will never change.
4. Expected output
    Subtotal: $82.9
    Tax at 8.0%: $5.60
    Tip at 20.0%: $17.70
    Grand Total: $106.19

"""

ORANGE_COUNTY_TAX_RATE = 0.08
TIP_FOR_GOOD_SERVICE = 0.2


def get_tip(bill_amount):
    return bill_amount * 0.20


def get_tax(subtotal):
    return subtotal * 0.0675


def print_receipt(subtotal):
    tax = get_tax(subtotal)
    bill_amount = subtotal + tax
    tip = get_tip(bill_amount)
    total = bill_amount + tip

    print("Subtotal: $" + str(subtotal))
    print("Tax at %s%%: $%.2f" % (ORANGE_COUNTY_TAX_RATE * 100, tax))     # %% to espcape % and print % itself
    print("Tip at {0}%: ${1:.2f}".format(TIP_FOR_GOOD_SERVICE * 100,  tip))
    print(f"Grand Total: ${total:.2f}")


# if calling this script directly, code below will be executed and serving as 'entry point'
# if importing funciton from this file, then code below will be ignored
if __name__ == '__main__':
    print_receipt(82.90)