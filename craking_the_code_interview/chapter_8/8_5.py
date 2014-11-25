def is_valid(paren):
	left = 0
	right = 0
	for c in paren:
		if c == "(":
			left += 1

		if c == ")":
			right += 1

		if left < right:
			return False
	return True


def get_valid_parentheses(n):
	paren = ""
	for i in range(n):
		paren += "("
	for i in range(n):
		paren += ")"

	permutations = get_permutations(paren)

	result = {}
	for p in permutations:
		if p in result:
			continue
		if is_valid(p):
			result[p] = True
	return result.keys()


def get_permutations(string):
	permutations = []
	if len(string) == 1:
		permutations.append(string)
		return permutations

	first = string[0]
	remainder = string[1:]
	rest_permutations = get_permutations(remainder)
	for p in rest_permutations:
		for i in range(len(p)+1):
			perm = p[:i] + first + p[i:]
			permutations.append(perm)
	return permutations


def get_all_parentheses(n):
	records = []
	add_parentheses(n, n, "", records)
	return records


def add_parentheses(left, right, string, records):
	if (left < 0) or (right < 0):
		return

	if (left == 0) and (right == 0):
		records.append(string[:])
		return

	if left > 0:
		string += "("
		add_parentheses(left-1, right, string, records)
		string = string[:-1]

	if (right > 0) and (left < right):
		string += ")"
		add_parentheses(left, right-1, string, records)
		string = string[:-1]


def main():
	print get_valid_parentheses(3)
	print get_all_parentheses(3)


if __name__ == "__main__":
	main()