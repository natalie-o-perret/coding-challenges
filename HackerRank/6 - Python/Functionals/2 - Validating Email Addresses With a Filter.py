import re

N = int(input())
regex = re.compile("^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$")
emails = [input() for _ in range(N)]
valid_emails = filter(regex.match, emails)
print (sorted(valid_emails))
