#!/usr/bin/env python

def replaceSpaceWithCharacter(string, character):
	return string.replace(' ', character)

def main():
	print replaceSpaceWithCharacter("hello, world", "%20")

if __name__ == "__main__":
	main()