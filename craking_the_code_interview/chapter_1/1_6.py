#!/usr/bin/env python
import random

'''
def rotate90Degree(matrix):
	n = len(matrix)
	result = [([0] * n) for i in range(n)]
	for i in range(n):
		for j in range(n):
			result[j][n-i-1] = matrix[i][j]
	return result
'''

def rotate90Degree(matrix):
	n = len(matrix)
	for i in range(n / 2):
		for j in range(i, n - i - 1):
			temp = matrix[i][j]
			matrix[i][j] = matrix[n - j - 1][i]
			matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
			matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
			matrix[j][n - i - 1] = temp
	return matrix


def randomInitial(matrix):
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			matrix[i][j] = random.randint(0, n)

def main():
	n = 3
	matrix = [([0] * n) for i in range(n)]
	randomInitial(matrix)
	print matrix

	rotate90Degree(matrix)
	print matrix

if __name__ == "__main__":
	main()