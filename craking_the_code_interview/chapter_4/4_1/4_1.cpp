#include <iostream>
#include "../tree.h"

using std::cout;
using std::endl;

int main()
{
	BinarySearchTree tree;
	tree.insert_node(2);
	tree.insert_node(1);
	tree.insert_node(3);

	cout << "Pre order traversal:" << endl;
	cout << tree.pre_order_traversal() << endl;

	cout << "In order traversal:" << endl;
	cout << tree.in_order_traversal() << endl;

	cout << "Post order traversal:" << endl;
	cout << tree.post_order_traversal() << endl;

	cout << "Does this tree is balanced?" << endl;
	cout << tree.is_balanced() << endl;

	return 0;
}