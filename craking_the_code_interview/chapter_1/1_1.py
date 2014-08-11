#!/usr/bin/env python

def determineIfAllUniqueCharacters(string):
	characters = list(string)
	result = {}
	for char in characters:
		if char in result:
			return False
		else:
			result[char] = True
	return True

def main():
	print determineIfAllUniqueCharacters("aaa")
	print determineIfAllUniqueCharacters("bbb")
	print determineIfAllUniqueCharacters("ccc")
	print determineIfAllUniqueCharacters("abc")

if __name__ == "__main__":
    main()