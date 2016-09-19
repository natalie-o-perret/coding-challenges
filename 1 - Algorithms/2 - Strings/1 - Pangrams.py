import string


def is_pangram(s):
    occurences = dict()
    alphabet = set(string.ascii_lowercase)
    for letter in s:
        letter = letter.lower()
        if letter in alphabet:
            if letter in occurences:
                occurences[letter] += 1
            else:
                occurences[letter] = 1
    return len(occurences) == len(string.ascii_lowercase)


s = input()
if is_pangram(s):
    print("pangram")
else:
    print("not pangram")
