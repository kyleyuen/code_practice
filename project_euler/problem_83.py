#!/usr/bin/env python

import sys   
sys.setrecursionlimit(10000)

def read_matrix(file_path):
	matrix = []
	with open(file_path, "r") as input:
		for line in input:
			matrix.append(map(int, line.split(",")))
	return matrix


def dfs(matrix, i, j, n, state, result, record):
	state[i][j] = False
	result += matrix[i-1][j-1]

	if i==n and j==n:
		if record[0] > result:
			record[0] = result
		state[i][j] = True
		return

	# north
	if state[i-1][j]:
		dfs(matrix, i-1, j, n, state, result, record)

	# east
	if state[i][j+1]:
		dfs(matrix, i, j+1, n, state, result, record)

	# south
	if state[i+1][j]:
		dfs(matrix, i+1, j, n, state, result, record)

	# west
	if state[i][j-1]:
		dfs(matrix, i, j-1, n, state, result, record)

	state[i][j] = True


def find_minimal_sum_path(matrix):
	n = len(matrix)
	state = [[True for i in range(n+2)] for j in range(n+2)]
	for i in range(n+2):
		state[i][0] = False
		state[i][n+1] = False
		state[0][i] = False
		state[n+1][i] = False

	record = [1e6]
	dfs(matrix, 1, 1, n, state, 0, record)
	return record[0]


def main():
	file_path = "p083_matrix.txt"
	matrix = read_matrix(file_path)
	print find_minimal_sum_path(matrix)


if __name__ == "__main__":
	main()