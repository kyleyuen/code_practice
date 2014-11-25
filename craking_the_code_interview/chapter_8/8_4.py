def get_permutations(array):
	permutations = []
	if len(array) == 1:
		permutations.append([array[0]])
		return permutations

	first = array[0]
	remainder = array[1:]
	rest_permutations = get_permutations(remainder)
	for p in rest_permutations:
		for i in range(len(p)+1):
			perm = p[:]
			perm.insert(i, first)
			permutations.append(perm)
	return permutations


def main():
	print get_permutations([i for i in range(1, 4)])


if __name__ == "__main__":
	main()