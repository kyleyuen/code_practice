#!/usr/bin/env python

def generate_next_state(pattern):
	next_state = [0 for i in range(len(pattern))]
	next_state[0] = -1

	k = -1
	j = 0
	while j+1 < len(pattern):
		if (k == -1) or (pattern[j] == pattern[k]):
			k += 1
			j += 1
			next_state[j] = k
		else:
			k = next_state[k]

	return next_state


def kmp(string, pattern):
	i = 0
	j = 0
	next_state = generate_next_state(pattern)

	while (i < len(string) and j < len(pattern)):
		if (j == -1) or (string[i] == pattern[j]):
			i += 1
			j += 1
		else:
			j = next_state[j]

	if j == len(pattern):
		return i - j
	else:
		return -1


def main():
	string = "abcabcd"
	pattern = "cabc"
	print kmp(string, pattern)


if __name__ == "__main__":
	main()