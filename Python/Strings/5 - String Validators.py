s = input()
meths = ["isalnum", "isalpha", "isdigit", "islower", "isupper"]
[print(any(getattr(c, meth)() for c in s)) for meth in meths]
