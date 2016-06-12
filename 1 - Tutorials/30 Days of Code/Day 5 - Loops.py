#!/bin/python3

import sys


N = int(input().strip())

for i in range(1, 11):
    print('{1} x {2} = {3}'.format(N, i, N * i))
