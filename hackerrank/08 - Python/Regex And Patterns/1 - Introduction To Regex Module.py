import re

T = int(input())
for _ in range(T):
    N = input()
    float_regex = re.compile("^[+-]?\d*\.\d+$")
    print(bool(float_regex.match(N)))
