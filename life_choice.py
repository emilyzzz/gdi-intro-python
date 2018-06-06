health = 100

print("A vicious warg is chasing you.")
print("Options:")
print("1 - Hide in the cave.")
print("2 - Climb a tree.")
input_value = input("Enter your choice:")

if input_value == '1':                                              # note the colon
    print('You hide in a cave.')                                    # indented 4 spaces
    print('The warg finds you and injures your leg with its claws')
    health = health - 10                                            # assignment from right to left
    print('health=', health)
elif input_value == '2':
    print('You climb a tree.')
    print('The warg eventually looses interest and wanders off')

print("Game under construction. Come back later")

