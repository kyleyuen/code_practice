#!/usr/bin/env python

def reverseString(string):
	characters = list(string)
	characters.reverse()
	return ''.join(characters)

def main():
	print reverseString("abc")
	print reverseString("cba")
	print reverseString("aaa")

if __name__ == "__main__":
	main()