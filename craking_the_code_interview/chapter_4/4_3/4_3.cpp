#include <iostream>
#include <vector>
#include "../tree.h"

using std::vector;
using std::cout;
using std::endl;

int main()
{
	BinarySearchTree tree;
	vector<int> array;
	for (int i = 1; i < 5; ++i) {
		array.push_back(i);
	}

	tree.create_minimal_height_tree(array);
	cout << tree.pre_order_traversal() << endl;
	cout << tree.in_order_traversal() << endl;
	cout << tree.post_order_traversal() << endl;
	return 0;
}