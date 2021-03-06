#include <iostream>
#include "../list.h"

using std::cout;
using std::endl;

int main()
{
	SingleLinkedList list;

	list.insert_node(1);
	list.insert_node(2);
	list.insert_node(3);
	list.insert_node(4);
	list.insert_node(5);

	cout << "Before remove node:" << endl;
	cout << list.to_string() << endl;

	cout << "After remove node:" << endl;
	Node* target = list.get_nth_node(2);
	list.delete_node_in_the_middle(target);
	cout << list.to_string() << endl;

	return 0;
}