#!/usr/bin/env python

def read_matrix(file_path):
	matrix = []
	with open(file_path, "r") as input:
		for line in input:
			matrix.append(map(int, line.split(",")))
	return matrix


def find_minimal_path_sum(matrix):
	n = len(matrix)
	dp = [[0 for i in range(n)] for j in range(n)]

	for i in range(n):
		dp[i][0] = matrix[i][0]

	for j in range(1, n):
		# get matrix[i][j:k]
		temp_array = [[0 for x in range(n)] for y in range(n)]
		for x in range(n):
			temp_array[x][x] = matrix[x][j]
			for y in range(x+1, n):
				temp_array[x][y] = temp_array[x][y-1] + matrix[y][j]

		for i in range(n):
			dp[i][j] = 1e6
			for k in range(n):
				if k < i:
					temp_value = temp_array[k][i]
				else:
					temp_value = temp_array[i][k]

				if dp[i][j] > dp[k][j-1] + temp_value:
					dp[i][j] = dp[k][j-1] + temp_value

	result = 1e6
	for i in range(n):
		if result > dp[i][n-1]:
			result = dp[i][n-1]
	return result


def main():
	file_path = "./p082_matrix.txt"
	matrix = read_matrix(file_path)
	print find_minimal_path_sum(matrix)


if __name__ == "__main__":
	main()