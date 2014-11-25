#!/usr/bin/env python

def gcd(a, b):
	while b != 0:
		c = a % b
		a = b
		b = c
	return a


def main():
	print gcd(3, 5)
	print gcd(3, 6)
	print gcd(8, 12)


if __name__ == "__main__":
	main()