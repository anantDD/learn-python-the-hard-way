def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


# run help(ex25)   and   help(ex25.break_words)
# the documentation that is coming up is generated from """ strings that we write. These are called documentation comments.

# functions learnt
#   ''.split()
#   sorted([])
#   [].pop()   .pop(0) for first  .pop(-1) for last

# to import
#   import ex25
#   from ex25 import *  (this places all the functions inside the current file)
