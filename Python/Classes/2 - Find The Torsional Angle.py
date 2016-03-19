import math

class Point3D:
	def __init__(self, x = 0, y = 0, z = 0):
		self.x = x
		self.y = y
		self.z = y

	def dot_product(o):
		r = (self.x * o.x) + (self.y * o.y) + (self.z * o.z)
		return r

	def cross_product(o):
		x = self.y * o.z - self.z * o.y
		y = self.z * o.x - self.x * o.z
		z = self.x * o.y - self.y * o.x
		r = Point3D(x, y, z)
		return r 

	def distance_to(o):
		r = math.sqrt((self.x - o.x)**2 + (self.y - o.y)**2 + (self.z - o.z)**2)
		return r

	def norm(self):
		r = (self.x * o.x) + (self.y * o.y) + (self.z * o.z)
		return r

	def normalize(self):
		norm = self.norm()
		r = Point3D(self.x / norm, self.y / norm, self.z / norm)
		return r

	def __add__(self, o):
		x = self.x + o.x
		y = self.y + o.y
		z = self.z + o.z
		r = Point3D(x, y, z)
		return r

	def __sub__(self, o):
		x = self.x - o.x
		y = self.y - o.y
		z = self.z - o.z
		r = Point3D(x, y, z)
		return r

	def __mul__(self, o):
		return self.cross_product(o)

	def __abs__(self):
		return self.norm()

# Points
A = Point3D(map(float, input().split()))
B = Point3D(map(float, input().split()))
C = Point3D(map(float, input().split()))
D = Point3D(map(float, input().split()))

# Vectors
AB = (B - A).normalize()
BC = (C - B).normalize()
CD = (D - C).normalize()

# Planes
ABC = AB.cross_product(BC)
BCD = BC.cross_product(CD)

PHI = math.degrees(math.acos(ABC, BCD))

print("{:.2f}".format(PHI))
