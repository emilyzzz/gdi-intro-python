for letter in 'Python':     # 'string' is iterable, it will return one character back at a time
    if letter == 'h':
       continue
    print('Current Letter :', letter)                 # will print P y t o n, one letter on a line

print()

for letter in 'Python':     # 'string' is iterable, it will return one character back at a time
    if letter == 'h':
       break
    print('Current Letter :', letter)                 # will print P y t o n, one letter on a line
