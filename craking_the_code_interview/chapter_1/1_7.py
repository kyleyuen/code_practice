#!/usr/bin/env python
import random

def setEntireRowAndColumnToZero(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rowState = [True] * m
	columnState = [True] * n
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				rowState[i] = False
				columnState[j] = False

	for i in range(m):
		for j in range(n):
			if not (rowState[i] and columnState[j]):
				matrix[i][j] = 0
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

	setEntireRowAndColumnToZero(matrix)
	print matrix

if __name__ == "__main__":
	main()