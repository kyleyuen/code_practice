#!/usr/bin/env python

def print_out_all_possibilities_in_two_ways():
	p = 0
	for i in range(100):
		p += 0.01
		a = p
		b = p * p * (1-p) * 3 + p * p * p
		print a, '\t', b


def main():
	print_out_all_possibilities_in_two_ways()


if __name__ == "__main__":
	main()