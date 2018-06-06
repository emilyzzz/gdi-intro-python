print('begin')


def reverse_sentence_1():
    sentence = input("Please input a sentence: ")
    length = len(sentence)
    i = length - 1
    new_sentence = ''
    while i >= 0:
        new_sentence = new_sentence + sentence[i]
        i = i - 1                                      # same as:  i -= 1
    print(new_sentence)


def reverse_sentence_2():
    sentence = input("Please input a sentence: ")
    print(sentence[::-1])


reverse_sentence_1()
print()
reverse_sentence_2()
