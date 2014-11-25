#!/usr/bin/env python

def paint_fill(color, point_x, point_y, screen, size, states):
	screen[point_x][point_y] = color
	states[point_x][point_y] = True

	if (point_x != 0) and (states[point_x-1][point_y] != True):
		paint_fill(color, point_x-1, point_y, screen, size, states)

	if (point_y + 1 != size) and (states[point_x][point_y+1] != True):
		paint_fill(color, point_x, point_y+1, screen, size, states)

	if (point_x + 1 != size) and (states[point_x+1][point_y] != True):
		paint_fill(color, point_x+1, point_y, screen, size, states)

	if (point_y != 0) and (states[point_x][point_y-1] != True):
		paint_fill(color, point_x, point_y-1, screen, size, states)


def main():
	screen = [[x for x in range(5)] for row in range(5)]
	states = [[False for x in range(5)] for row in range(5)]
	print screen

	paint_fill(1, 3, 3, screen, 5, states)
	print screen


if __name__ == "__main__":
	main()