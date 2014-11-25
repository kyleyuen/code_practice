def get_all_subsets(array):
	subsets = []
	current_set = set()
	get_subset(array, 0, current_set, subsets)
	return subsets



def get_subset(array, index, current_set, subsets):
	if len(array) == index:
		subsets.append(current_set.copy())
		return

	get_subset(array, index+1, current_set, subsets)
	
	current_set.add(array[index])
	get_subset(array, index+1, current_set, subsets)
	current_set.remove(array[index])



def main():
	print get_all_subsets([1, 2, 3])



if __name__ == "__main__":
	main()