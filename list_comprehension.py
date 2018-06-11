# two ways to form a new list, that's the square of even members only.

def get_even_square(nums):
    # Form new list by 'for loop',

    # Initialize `new_list`
    new_list = []

    # Add values to `new_list`
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n**2)

    return new_list


def get_even_square_list_comprehension(nums):
    new_list = [ x**2 for x in nums if x % 2 == 0 ]
    return new_list


numbers = range(10)
new_list1 = get_even_square(numbers)
print("The new list formed by looping and list.append() method: ", new_list1)
new_list2 = get_even_square_list_comprehension(numbers)
print("The new list formed by list comprehension: ", new_list2)
