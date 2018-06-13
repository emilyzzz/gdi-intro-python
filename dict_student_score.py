"""
Objective
    1. review list
    2. review dict
    3. string formatting
    4. review function: def, input argument, input arg with default (see notes)
    5. flow control: if, break, for loop
"""

import random           # import always on top, unless there's technical reason not to (rare)


def get_score_list():
    """
    return a list of 100 student grades: [ [student_id1,  98],  [student_id2,  76], ... ]
    student_id/score are generated randomly
    """
    grades = []
    for _ in range(100):
        student_id = random.randint(100000, 999999)
        score = random.randint(60, 100)
        grades.append([student_id, score])

    return grades


def convert_list_to_dict(input_list):
    """
    Convert input grades of list type into dict data structure
    input_list: [ [student_id1,  98],  [student_id2,  76], ... ]
    output: { student_id1: 98,   student_id2: 76, ... }
    """
    my_dict = {}
    for ea in input_list:
        student_id = ea[0]              # or use:   student_id, score = ea
        score = ea[1]
        my_dict[student_id] = score

    return my_dict


def print_dict(input_dict, n=5):
    """
    nicely print the dict

    Params:
        input_dict: { student_id1: 98,   student_id2: 76, ... }
        n: number of data to print, by default, print 5 entries.

    Example output:
        The score for student: student_id1 is 98
        The score for student: student_id2 is 76
    """

    count = 0
    for k, v in input_dict.items():
        print('Student with id=%s has score=%s' % (k, v))
        count += 1
        if count >= n:
            break


grades_list = get_score_list()
print('\nFirst 3 entries in grades_list: ', grades_list[:3])

grades_dict = convert_list_to_dict(grades_list)

print()
print_dict(grades_dict)         # n=5, the default
print()

print_dict(grades_dict, n=2)    # n=2, overriding default
print()

print_dict(grades_dict, 2)      # n=2, overriding default
print()







