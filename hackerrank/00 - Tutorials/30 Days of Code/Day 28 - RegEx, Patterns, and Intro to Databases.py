import re


gmail_regex = re.compile("^[a-z\.]+@gmail.com$")
gmail_accounts = dict()
N = int(input().strip())
for _ in range(N):
	firstName, email = input().strip().split(' ')
	if gmail_regex.match(email):
		gmail_accounts[email] = firstName

sorted_names = sorted(gmail_accounts.values())
print(*sorted_names, sep="\n")
