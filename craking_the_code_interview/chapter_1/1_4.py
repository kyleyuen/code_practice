#!/usr/bin/env python

def decideIfTwoStringsAreAnagrams(stra, strb):
	charactersA = splitStringToCharactersDict(stra)
	charactersB = splitStringToCharactersDict(strb)
	return charactersA == charactersB

def splitStringToCharactersDict(string):
	characters = list(string)
	result = {}
	for char in characters:
		if char in result:
			result[char] += 1
		else:
			result[char] = 1
	return result

def main():
	print decideIfTwoStringsAreAnagrams("aaa", "aaa")
	print decideIfTwoStringsAreAnagrams("aaa", "bbb")
	print decideIfTwoStringsAreAnagrams("abc", "cba")
	print decideIfTwoStringsAreAnagrams("aabcc", "cabca")

if __name__ == "__main__":
	main()