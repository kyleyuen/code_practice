#!/usr/bin/env python

def find_longest_ascending_sequence(array):
	dp = [0 for i in range(len(array))]
	for i in range(len(array)):
		max_length = 0
		for j in range(i):
			if array[j] < array[i] and dp[j] > max_length:
				max_length = dp[j]
		dp[i] = max_length + 1
	return dp[len(array)-1]


def find_longest_ascending_sequence_with_save(array):
	answer = []
	for i in range(len(array)):
		answer_length = len(answer)
		if answer_length == 0 or array[i] > answer[answer_length-1]:
			answer.append(array[i])

		for j in range(len(answer)-1, -1, -1):
			if array[i] > answer[j]:
				answer[j+1] = array[i]
				break
		if answer[0] > array[i]:
			answer[0] = array[i]
	return len(answer)



def main():
	array = [4, 5, 1, 2, 3, 1, 2, 3, 4]
	#print find_longest_ascending_sequence(array)
	print find_longest_ascending_sequence_with_save(array)


if __name__ == "__main__":
	main()