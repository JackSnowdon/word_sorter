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


def add_word():
    word = input("Type word to add to array: ")
    if word.isdigit():
        print("Input needs to be string!")
        add_word()
    print(f"Added '{word}'")
    wordarray.append(word)
    check()


def remove_word():
    for i, word in enumerate(wordarray): 
        print (f"{i+1}: {word}")
    choice = input("Type number to delete or 'b' to go back: " )
    if choice.isdigit():
        try:
            to_delete = wordarray[int(choice) - 1]
            print(f"Revmoed {to_delete} from Array")
            wordarray.remove(to_delete)
            check()
        except:
            print("Not a valid selection")
            remove_word()
    elif choice == 'b':
        check()
    else:
        print("Not an int selection")
        remove_word()


def check():
    print(f"Current Words: {wordarray}")
    cmd = input("Type 'add' or 'remove' to work with array, or 'run' to start task ('q' to quit): ")
    if cmd == 'run':
        result = sort_words(wordarray)
        print(f"Returned Words: {result}")
        again = input("Run Again y/n: ")
        if again == 'y':
            check()
        else: 
            print("Thanks for using the word checker!")
    elif cmd == 'add':
        add_word()
    elif cmd == 'remove':
        remove_word()
    elif cmd == 'q':
        print("Thanks for using the word checker!")
    else:
        print(f"'{cmd}' not valid entry")
        check()

check()

"""
This task was more suited to my python skills, resulting in neater code.
To refactor I would look at quicker way to replace the letters
without creating a new list.
"""