N = int(input())
fib = lambda x: x if (x < 2) else (fib (x - 1) + fib (x - 2))
# print (map(lambda x: x**3, map(fib, range(N))))
print ([fib(x)**3 for x in range(N)])
