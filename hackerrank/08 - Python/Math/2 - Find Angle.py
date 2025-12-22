import cmath

z = complex(input())
AB = int(input())
BC = int(input())
A = complex(0, AB)
B = complex(0, 0)
C = complex(BC, 0)
print(phase(B + C + A))


MBC = cmath.atan(BC/AC)
print(MBC)
