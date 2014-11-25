def move_right_and_down(x, y, n):
	if x == n:
		if y == n - 1:
			return 1
		else:
			return move_right_and_down(x, y+1, n)

	if y == n:
		if x == n - 1:
			return 1
		else:
			return move_right_and_down(x+1, y, n)

	return move_right_and_down(x+1, y, n) + move_right_and_down(x, y+1, n)



def main():
	print move_right_and_down(1, 1, 10)



if __name__ == "__main__":
	main()