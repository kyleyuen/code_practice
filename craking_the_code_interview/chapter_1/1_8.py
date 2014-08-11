#!/usr/bin/env python

def checkIfRotationString(stra, strb):
	return strb in (stra * 2)

def main():
	stra = "waterbottle"
	strb = "erbottlewat"
	print checkIfRotationString(stra, strb)

if __name__ == "__main__":
	main()