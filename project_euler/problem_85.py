#!/usr/bin/env python

def counting_rectangels(row, column):
	result = 0
	for i in range(1, row+1):
		for j in range(1, column+1):
			temp = (row-i+1) * (column-j+1)
			result += temp
	return result


def main():
	upper_bound = 100
	area = 0
	counter = 2000000
	for i in range(upper_bound):
		for j in range(upper_bound):
			result = counting_rectangels(i, j)
			if counter > abs(result-2000000):
				counter = abs(result-2000000)
				area = i * j
	print area


if __name__ == "__main__":
	main()