#!/bin/python3

import sys


N = int(input().strip())

for i in range(1, 11):
    print('{0} x {1} = {2}'.format(N, i, N * i))
