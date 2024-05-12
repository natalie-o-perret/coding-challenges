import math


class Complex:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		if self.y >= 0:
			return "{:.2f}+{:.2f}i".format(self.x, self.y)
		else:
			return "{:.2f}{:.2f}i".format(self.x, self.y)

	def __add__(self, o):
		x = self.x + o.x
		y = self.y + o.y
		r = Complex(x, y)
		return r

	def __sub__(self, o):
		x = self.x - o.x
		y = self.y - o.y
		r = Complex(x, y)
		return r

	def __mul__(self, o):
		x = self.x * o.x - self.y * o.y
		y = self.x * o.y + self.y * o.x
		r = Complex(x, y)
		return r   

	def __truediv__(self, o):
		x = (self.x * o.x + self.y * o.y) / (o.x**2 + o.y**2)
		y = (self.y * o.x - self.x * o.y) / (o.x**2 + o.y**2)
		r = Complex(x, y)
		return r

	def __abs__(self):
		x = math.sqrt(self.x**2 + self.y**2)
		r = Complex(x)
		return r


Cr, Ci = map(float, input().split())
Dr, Di = map(float, input().split())
C = Complex(Cr, Ci)
D = Complex(Dr, Di)

print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(abs(C))
print(abs(D))
