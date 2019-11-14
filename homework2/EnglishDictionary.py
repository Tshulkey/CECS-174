__dictionary__ = None
try:
    __dictionary__ = set(map(lambda s: s.strip(), open("words_alpha.txt")))
except IOError:
    print("Could not open the file words_alpha.txt. Please make sure it is in the same folder as your .py file.")


def is_word(string):
    return string in __dictionary__
