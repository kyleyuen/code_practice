#include <iostream>
#include "../list.h"
#include "../utility.h"

using std::cout;
using std::endl;

int main()
{
	SingleLinkedList left;
	SingleLinkedList right;

	left.insert_node(5);
	left.insert_node(1);
	left.insert_node(3);

	right.insert_node(2);
	right.insert_node(9);
	right.insert_node(7);

	cout << "Left hand list:" << endl;
	cout << left.to_string() << endl;

	cout << "right hand list:" << endl;
	cout << right.to_string() << endl;
	
	SingleLinkedList result = add_two_lists(left, right);
	cout << "add two lists:" << endl;
	cout << result.to_string() << endl;

	return 0;
}