#!/usr/bin/env python

def convert(number, result):
	length = len(number)
	if length == 0:
		print ''.join(result)
		return
	
	digit = number[0]
	character = chr(ord('a')-1+int(digit))
	result.append(character)
	convert(number[1:], result)
	result.pop()

	if length > 1:
		digits = number[0:2]
		if int(digits) > 26:
			return

		character = chr(ord('a')-1+int(digits))
		result.append(character)
		convert(number[2:], result)
		result.pop()


def main():
	result = []
	convert("12258", result)


if __name__ == "__main__":
	main()