#!/usr/bin/env python

number_of_queens = 8

def eight_queens():
	board = [[0 for i in range(number_of_queens)] for j in range(number_of_queens)]
	dfs(board, 0)


def is_conflict(board, row, column):
	for i in range(row):
		if board[i][column] == 1:
			return True

	for i in range(1, min(row, column)+1):
		if board[row - i][column - i] == 1:
			return True

	for i in range(1, min(row, number_of_queens-column-1)+1):
		if board[row - i][column + i] == 1:
			return True

	return False

def dfs(board, n):
	if n == number_of_queens:
		print board

	for j in range(number_of_queens):
		if not is_conflict(board, n, j):
			board[n][j] = 1
			dfs(board, n+1)
			board[n][j] = 0


def main():
	eight_queens()


if __name__ == "__main__":
	main()