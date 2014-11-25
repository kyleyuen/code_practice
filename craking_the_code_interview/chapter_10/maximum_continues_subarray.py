#!/usr/bin/env python

def linear_search(array):
	result = array[0]
	summation = 0

	for i in range(len(array)):
		if summation >= 0:
			summation += array[i]
		else:
			summation = array[i]

		if result < summation:
			result = summation

	return result


def dp_search(array):
	dp = [0 for i in range(len(array))]
	dp[0] = array[0]
	
	for i in range(1, len(array)):
		if array[i] < dp[i-1] + array[i]:
			dp[i] = dp[i-1] + array[i]
		else:
			dp[i] = array[i]

	result = dp[0]
	for i in range(1, len(dp)):
		if result < dp[i]:
			result = dp[i]

	return result




def main():
	array = [1, -2, 3, 10, -4, 7, 2, -5]
	#print linear_search(array)
	print dp_search(array)

	array = [-1, -2, -3, -4]
	#print linear_search(array)
	print dp_search(array)


if __name__ == "__main__":
	main()