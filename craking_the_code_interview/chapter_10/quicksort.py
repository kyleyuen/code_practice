#!/usr/bin/env python

import random

def quick_sort(array, start, end):
	if start < end:
		position = partition(array, start, end)
		quick_sort(array, start, position)
		quick_sort(array, position+1, end)


def partition(array, start, end):
	pivot = array[end-1]
	pos = start
	for i in range(start, end-1):
		if array[i] < pivot:
			temp = array[pos]
			array[pos] = array[i]
			array[i] = temp
			pos += 1
	array[end-1] = array[pos]
	array[pos] = pivot
	return pos


def check_correctness(array):
	if len(array) == 1:
		return True
	for i in range(1, len(array)):
		if array[i-1] > array[i]:
			return False
	return True

def main():
	array = []
	for i in range(100):
		array.append(random.randint(1, 100))
	quick_sort(array, 0, len(array))
	print check_correctness(array)
	print array


if __name__ == "__main__":
	main()