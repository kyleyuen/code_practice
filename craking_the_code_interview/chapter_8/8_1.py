def fibonacci(n):
	if n < 0:
		return 0

	if (n == 0) or (n == 1):
		return 1

	return fibonacci(n - 1) + fibonacci(n - 2)


def main():
	print fibonacci(5)


if __name__ == "__main__":
	main()