def function_with_default_arg(message, n=0., values=None):                # 0. is same as 0.0,  5. == 5.0
   if values is None:
       values = 'UNKNOWN'
   print("\tInput n =", n)                                        # "\t" :  tab
   print("\tInput message =", message)
   print("\tInput values =", values, '\n')


# calling with only required input arg
function_with_default_arg('Display Message')

# calling with required arg and optional keyword arg
function_with_default_arg('Display Message', n=20)               # n is called 'keyword argument'

# calling with required arg and optional arg
function_with_default_arg('Display Message', values='Good')

# calling with required arg and optional arg, the order of 'keyword args' can be switched
function_with_default_arg('Display Message', n=100, values='Good')
function_with_default_arg('Display Message', values='Good', n=100)