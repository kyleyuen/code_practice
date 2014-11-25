#!/usr/bin/env python

def represent_n_cents(n):
	coins = [1, 5, 10, 25, 50, 100]
	coin_type = len(coins)
	ways = [[0 for i in range(coin_type)] for j in range(n+1)]

	for i in range(n+1):
		ways[i][0] = 1

	for i in range(n+1):
		for j in range(1, coin_type):
			counter = int(i / coins[j])
			for k in range(counter+1):
				ways[i][j] += ways[i-k*coins[j]][j-1]
	return ways[n][coin_type-1]


def main():
	print represent_n_cents(100)


if __name__ == "__main__":
	main()