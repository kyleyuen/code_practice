#!/usr/bin/env python

def multiply(a, b):
	result = 0
	for i in range(b):
		result += a
	return result


def minus(a, b):
	result = a + multiply(b, -1)
	return result


def divide(a, b):
	if b == 0:
		return
		
	result = 0
	while (a >= b):
		a -= b
		result += 1
	return result


def main():
	print minus(6, 3)
	print multiply(6, 3)
	print divide(6, 3)


if __name__ == "__main__":
	main()