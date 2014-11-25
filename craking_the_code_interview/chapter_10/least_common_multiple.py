#!/usr/bin/env python

from greatest_common_divisor import gcd

def lcm(a, b):
	return a * b / gcd(a, b)


def main():
	print lcm(3, 5)
	print lcm(3, 6)
	print lcm(8, 12)


if __name__ == "__main__":
	main()