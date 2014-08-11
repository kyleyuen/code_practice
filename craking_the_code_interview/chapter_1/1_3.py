#!/usr/bin/env python

def removeDuplicateCharacters(string):
	characters = list(string)
	state = {}
	counter = 0
	for char in characters:
		if char not in state:
			state[char] = True
			characters[counter] = char
			counter += 1
	return ''.join(characters[:counter])

def main():
	print removeDuplicateCharacters("aaaaa")
	print removeDuplicateCharacters("abcba")
	print removeDuplicateCharacters("abcabc")
	print removeDuplicateCharacters("cbacba")
	print removeDuplicateCharacters("aabbcc")

if __name__ == "__main__":
	main()