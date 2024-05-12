import math


class Point3D(object):
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return "{:.2f}".format(self.x, self.y, self.y)


class Vector3D(object):
	def __init__(self, start_point=Point3D(), stop_point=Point3D()):
		self.x = stop_point.x - start_point.x
		self.y = stop_point.y - start_point.y
		self.z = stop_point.z - start_point.z

	def dot_product(self, other):
		r = (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
		return r

	def cross_product(self, other):
		r = Vector3D()
		r.x = self.y * other.z - self.z * other.y
		r.y = self.z * other.x - self.x * other.z
		r.z = self.x * other.y - self.y * other.x
		return r

	def distance_to(self, other):
		r = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
		return r

	def norm(self):
		r = self.distance_to(Vector3D())
		return r

	def __add__(self, other):
		r = Vector3D()
		r.x = self.x + other.x
		r.y = self.y + other.y
		r.z = self.z + other.z
		return r

	def __sub__(self, other):
		r = Vector3D()
		r.x = self.x - other.x
		r.y = self.y - other.y
		r.z = self.z - other.z
		return r

	def __mul__(self, other):
		return self.cross_product(other)

	def __abs__(self):
		return self.norm()


# Points
A = Point3D(*list(map(float, input().split())))
B = Point3D(*list(map(float, input().split())))
C = Point3D(*list(map(float, input().split())))
D = Point3D(*list(map(float, input().split())))

# Vectors
AB = Vector3D(A, B)
BC = Vector3D(B, C)
CD = Vector3D(C, D)

# Planes: ABC and BCD
X = AB * BC
Y = BC * CD

# Angle
PHIrad = math.acos(X.dot_product(Y) / (abs(X) * abs(Y)))
PHIdeg = math.degrees(PHIrad)

print("{:.2f}".format(PHIdeg))
