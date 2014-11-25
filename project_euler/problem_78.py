#!/usr/bin/env python

def represent_n_coins(n):
	ways = [[0 for i in range(n+1)] for j in range(n+1)]

	for i in range(1, n+1):
		ways[i][i] = 1
		ways[i][1] = 1

	for i in range(1, n+1):
		for j in range(2, n+1):
			counter = int(i/j)
			for k in range(counter+1):
				ways[i][j] += ways[i-k*j][j-1]
	return ways[n][n]


def main():
	print represent_n_coins(53374)
	"""
	for i in range(1, 500):
		result =  represent_n_coins(i)
		print i, result
		if result % 1000000 == 0:
			print i
			break
	"""


if __name__ == "__main__":
	main()