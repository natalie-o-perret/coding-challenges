import string

n, alphabet = int(input()), string.ascii_lowercase
pattern = [("-".join(alphabet[n - 1 : n - i - 1 : -1] + alphabet[n - i - 1 : n])).center(4 * n - 3, "-") for i in range(n)]
print('\n'.join(pattern[ : -1] + pattern[ : : -1]))
