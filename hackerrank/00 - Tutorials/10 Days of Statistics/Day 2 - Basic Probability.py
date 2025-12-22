import math

# In a single toss of 2 fair (evenly-weighted) six-sided dice,
# find the probability that their sum will be at most 9.
from fractions import Fraction

dice_max = 6
dice_min = 1
dice_range = range(dice_min, dice_max + 1)
count = 0
for d1 in dice_range:
	for d2 in dice_range:
		if (d1 + d2) <= 9:
			count += 1
possibilities = dice_max**2
print(Fraction(count, possibilities))