#!/usr/bin/env python

def merge_two_sorted_arrays(first, valid_position, second):
	indexA = valid_position
	indexB = len(second) - 1
	insert_position = len(first) - 1

	while (indexA >= 0 and indexB >= 0):
		if (first[indexA] < second[indexB]):
			first[insert_position] = second[indexB]
			indexB -= 1
		else:
			first[insert_position] = first[indexA]
			indexA -= 1
		insert_position -= 1

	while (indexB >= 0):
		first[insert_position] = second[indexB]
		insert_position -= 1
		indexB -= 1

	return first


def main():
	first = [1, 3, 5, 6, 7]
	for i in range(5):
		first.append(0)

	second = [2, 4, 8, 9, 10]
	print merge_two_sorted_arrays(first, 4, second)


if __name__ == "__main__":
	main()