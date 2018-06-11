
def pre_process(text):
    """
    this function takes input of a string, return a list of lowercase words with punctuation removed
    """

    # convert all letters to lower case
    text = text.lower()

    # replace each punctuation character with a space, use str.replace() or str.strip() methods
    for ch in '!"#$%&()*+,-./:;<=>?@[3\\]^_\'{|}~':
        text = text.replace(ch, " ")

    # convert a string to list of words, plural 'words' implies a list
    words = text.split()
    return words


def word_count1(words):
    # check if a word is in the counts first. Returns dict of {word: count_of_word}
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1       # same as:  counts[w] = counts[w] + 1
        else:
            counts[w] = 1
    return counts


def word_count2(words):
    # use dict.get() method. Returns dict of {word: count_of_word}
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1     # if w exists in dict, get the value, if not, get 0
    return counts



def print_dict(counts):
    """
    print the dict
        using 'i' and 'max_rows' below is to control we only print 10 lines, instead of many lines for large doc
        note what gets printed may not be same words each time, since dict is unordered
    """
    i = 0
    max_rows = 10
    for k, v in counts.items():
        print('\tWord: {0:15s} Count: {1:>3}'.format(k+",", v))  # new style formatting with alignment control. ">": align right
        i += 1
        if i == max_rows:
            break                                                # 'break' will get out of a loop when "if condition" returns True



def main():
    f = open('zen_of_python.txt', 'r')
    text = f.read()
    words = pre_process(text)

    print('\nPrint Dict using counts from word_count1...')
    print_dict(word_count1(words))

    print('\nPrint Dict using counts from word_count2...')
    print_dict(word_count2(words))


main()