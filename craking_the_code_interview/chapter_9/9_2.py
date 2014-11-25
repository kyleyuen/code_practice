#!/usr/bin/env python

def insertion_sort(array):
	for i in range(1, len(array)):
		container = array[i]
		j = i - 1
		while j >= 0 and array[j] > container:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = container


def main():
	array = [chr(x) for x in range(ord('z'), ord('a')-1, -1)]
	insertion_sort(array)
	print array


if __name__ == "__main__":
	main()