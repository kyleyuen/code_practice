#!/usr/bin/env python

def find_number_index(array, lower, upper, number):
	middle = (lower + upper) / 2
	if array[middle] == number:
		return middle
	
	if array[lower] <= array[middle - 1]:
		if array[lower] <= number and number <= array[middle - 1]:
			return find_number_index(array, lower, middle, number)
		else:
			return find_number_index(array, middle, upper, number)
	if array[middle] <= array[upper - 1]:
		if array[middle] <= number and number <= array[upper - 1]:
			return find_number_index(array, middle, upper, number)
		else:
			return find_number_index(array, lower, middle, number)

	return -1

def main():
	array = [20, 25, 1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
	print find_number_index(array, 0, len(array), 19)
	return 0


if __name__ == "__main__":
	main()