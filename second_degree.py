import math
import sqrt

class solver:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.degree_1 = False
		self.no_solution = False
		self.negative_discriminant = False
		self.only_one_result = False
		self.infinite_results = False
		self.discriminant = (self.b * self.b) - (4 * self.a * self.c)
		self.denominator = 2 * self.a
		if (self.a == 0 and self.b == 0 and self.c == 0):
			self.infinite_results = True
		elif (self.a == 0):
			self.degree_1 = True
			if (self.b == 0 and self.c != 0):
				self.no_solution = True
			else:
				self.result_1 = -self.c / self.b
		elif (self.discriminant < 0):
			self.negative_discriminant = True
		else:
			if (self.discriminant == 0):
				self.only_one_result = True
			self.numerator_0 = -self.b + sqrt.solve(self.discriminant)
			self.numerator_1 = -self.b - sqrt.solve(self.discriminant)
			self.result_0 = self.numerator_0 / self.denominator
			self.result_1 = self.numerator_1 / self.denominator
			if (self.result_0 == 0 and self.result_1 == 0):
				self.infinite_results = True
