#!/usr/bin/env python

from fractions import Fraction


def find_nth_convergent_of_e(n):
	add_up = Fraction()
	counter = int((n+1)/3)
	for i in range(n, 0, -1):
		if i % 3 == 2:
			add_up = Fraction(1, add_up+counter*2)
			counter -= 1
		else:
			add_up = Fraction(1, add_up+1)
	return 2 + add_up


def sum_of_digits(num):
	result = 0
	for i in range(len(num)):
		result += int(num[i])
	return result


def main():
	num = find_nth_convergent_of_e(99)
	print str(num.numerator)
	print sum_of_digits(str(num.numerator))


if __name__ == "__main__":
	main()
