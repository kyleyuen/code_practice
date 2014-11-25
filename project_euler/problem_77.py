#!/usr/bin/env python

def get_primes(n):
	result = []
	sifter = [True for i in range(n+1)]
	for i in range(2, n):
		for j in range(i*2, n+1, i):
			sifter[j] = False

	for i in range(2, n+1):
		if sifter[i]:
			result.append(i)
	return result


def ways_of_prime_summation(n, primes):
	number_of_primes = len(primes)
	ways = [[0 for i in range(number_of_primes)] for j in range(n+1)]

	for i in range(n+1):
		if i % 2 == 0:
			ways[i][0] = 1

	for i in range(n+1):
		for j in range(1, number_of_primes):
			counter = int(i / primes[j])
			for k in range(counter+1):
				ways[i][j] += ways[i-k*primes[j]][j-1]
	return ways[n][number_of_primes-1]


def main():
	upper_bound = 100
	primes = get_primes(upper_bound)
	for i in range(upper_bound):
		print i, ways_of_prime_summation(i, primes)


if __name__ == "__main__":
	main()