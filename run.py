wordarray = ['Hello World', 'Goodbye World', 'World Gossip', 'Doll Loop Hell Teeth']

def sort_words(array):
    """
    Takes Array of strings
    Reverses the order
    Then checks each word in string, any repeated letters are both replaced
    with '*' by turning the word into a list, replacing letters and using join()
    Returns Sorted Array of Strs
    """
    sortedwords = []
    for word in wordarray:
        rev_w = ' '.join(reversed(word.split(' ')))
        last_letter = ''
        for i, l in enumerate(rev_w):
            if l == last_letter:
                listed_word = list(rev_w)
                listed_word[i-1] = '*'
                listed_word[i] = '*'
                rev_w = ''.join(listed_word)
            last_letter = l
        sortedwords.append(rev_w)
    return sortedwords

def command():
    print(f"Current Words: {wordarray}")
    return input("Type 'add' to add word, or 'run' to start task ('q' to quit): ")

def check(cmd):
    if cmd == 'run':
        result = sort_words(wordarray)
        print(f"Returned Words: {result}")
    elif cmd == 'q':
        print("Thanks for using the word checker!")
    else:
        print(f"'{cmd}' not valid entry")
        new = command()
        check(new)

cmd = command()
check(cmd)

"""
This task was more suited to my python skills, resulting in neater code.
To refactor I would look at quicker way to replace the letters
without creating a new list.
"""