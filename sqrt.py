import math

def solve(number):
	if (number == 0):
		return (0)
	x = number
	while (1):
		root = 0.5 * (x + (number / x))
		if (abs(root - x) < 0.000001):
			break
		x = root
	return (root)
