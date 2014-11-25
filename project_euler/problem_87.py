#!/usr/bin/env python

def get_primes(n):
	result = []
	sifter = [True for i in range(n+1)]
	for i in range(2, n+1):
		for j in range(i*2, n+1, i):
			sifter[j] = False

	for i in range(2, n+1):
		if sifter[i]:
			result.append(i)
	return result


def find_prime_power_triples(primes):
	records = set()
	for i in range(len(primes)):
		for j in range(len(primes)):
			for k in range(len(primes)):
				result = primes[i]**2 + primes[j]**3 + primes[k]**4
				#print result
				if result > 50000000:
					break
				records.add(result)
	return records


def main():
	primes = get_primes(8000)
	print len(find_prime_power_triples(primes))


if __name__ == "__main__":
	main()